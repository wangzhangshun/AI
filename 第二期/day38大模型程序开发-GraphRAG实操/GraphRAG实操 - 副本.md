

### 三、GraphRAG快速部署与调用方法详解

#### 1.GraphRAG安装

> 注，以下实验环境均为Ubuntu系统，以更好的模拟真实企业应用场景，其中大多数方法也可以直接迁移至Windows操作系统中。下面我们的操作以AutoDL平台上进行！

**Step 1.使用pip安装graphrag**

``pip install graphrag=0.5`` 

**Step 2.创建检索项目文件夹**

需要在任何合适的目录下创建一个任意名字的文件夹，该文件夹内部需要再创建一个名字固定为input的子文件夹，用于保存上传的数据集文件。``mkdir -p ./openl/input``

**Step 3.上传数据集**

将数据集文件上传至input目录下。只可以上传txt格式文件。

**Step 4.初始化项目文件**

初始化项目文件后，会生成GraphRAG项目需要的相关配置文件。

``graphrag init --root ./openl``

**Step 5.修改项目配置**

<img src="GraphRAG%E5%AE%9E%E6%93%8D.assets/image-20250605081703642.png" alt="image-20250605081703642" style="zoom:67%;" />

``注意：graphrag 本身只支持openai系列模型使用。而deepseek-v3和Qwen系列（如Qwen3-235B-A22B、Qwen3-4B）正好采用了和GPT模型完全一样的调用方法和输出格式。因此deepseek-v3和Qwen系列也是目前除GPT外可以无缝接入GraphRAG的大模型。``

- 打开.env文件（ls -all），填写大模型的 API-KEY。可以使用DeepSeek-V3模型何其对应的api_key

  ![image-20250605094318384](GraphRAG%E5%AE%9E%E6%93%8D.assets/image-20250605094318384.png)

- 打开setting.yaml文件，填写模型名称和base url：

  - DeepSeek-V3模型和向量模型，此处的向量模型使用的硅基流动中的Qwen/Qwen3-Embedding-8B为例。

  <img src="GraphRAG%E5%AE%9E%E6%93%8D.assets/image-20250730090539626.png" alt="image-20250730090539626" style="zoom:67%;" />

#### 2.Indexing检索流程实现

一切准备就绪后，即可开始执行GraphRAG索引过程。可以借助GraphRAG脚本自动执行indexing。

``graphrag index --root ./openl``

运行结束后，各知识图谱相关数据集都保存在output文件夹中：

<img src="GraphRAG%E5%AE%9E%E6%93%8D.assets/image-20250605092432538.png" alt="image-20250605092432538" style="zoom:67%;" />

#### 3.全局搜索问答实现

**GraphRAG v 0.5版本bug修复**

GraphRAG最新版 v0.5版本当使用OpenAI的Embedding模型时，会出现运行报错，此时需要修改lancedb.py文件才可正常运行。在Ubuntu服务器下，脚本文件地址如下：

<img src="GraphRAG%E5%AE%9E%E6%93%8D.assets/image-20250730085339817.png" alt="image-20250730085339817" style="zoom:67%;" />

autodl修改GraphRAG源码，源码路径：

``/root/miniconda3/lib/python3.12/site-packages/graphrag/vector_stores/lancedb.py``

打开脚本文件后需修改如下内容：

<img src="GraphRAG%E5%AE%9E%E6%93%8D.assets/image-20250730085441516.png" alt="image-20250730085441516" style="zoom:67%;" />

当使用Qwen/Qwen3-Embedding-8B向量模型时，需手动设置N = 4096。

**构建GlobalSearch（全局搜索）搜索引擎并进行问答**

模块导入：

```Python
import tiktoken
import pandas as pd
from graphrag.query.indexer_adapters import (
    read_indexer_communities,
    read_indexer_entities,
    read_indexer_reports,
)
from graphrag.query.llm.oai.chat_openai import ChatOpenAI
from graphrag.query.llm.oai.typing import OpenaiApiType
from graphrag.query.structured_search.global_search.community_context import (
    GlobalCommunityContext,
)
from graphrag.query.structured_search.global_search.search import GlobalSearch
```

数据加载与预处理：

```Python
INPUT_DIR = "./demo/output"
LANCEDB_URI = f"{INPUT_DIR}/lancedb"
COMMUNITY_LEVEL = 2 #社区层级

COMMUNITY_TABLE = "create_final_communities"
COMMUNITY_REPORT_TABLE = "create_final_community_reports"
ENTITY_TABLE = "create_final_nodes"
ENTITY_EMBEDDING_TABLE = "create_final_entities"

#相关指定数据加载，包含：实体表、社区表等
community_df = pd.read_parquet(f"{INPUT_DIR}/{COMMUNITY_TABLE}.parquet")
entity_df = pd.read_parquet(f"{INPUT_DIR}/{ENTITY_TABLE}.parquet")
report_df = pd.read_parquet(f"{INPUT_DIR}/{COMMUNITY_REPORT_TABLE}.parquet")
entity_embedding_df = pd.read_parquet(f"{INPUT_DIR}/{ENTITY_EMBEDDING_TABLE}.parquet")

#数据预处理：根据上面加载好的数据表格重构实体和社区报告等对象集合
#read_indexer_communities函数表示为特征解析器
communities = read_indexer_communities(community_df, entity_df, report_df)
reports = read_indexer_reports(report_df, entity_df, COMMUNITY_LEVEL)
entities = read_indexer_entities(entity_df, entity_embedding_df, COMMUNITY_LEVEL)
```

创建Global Search模式的上下文构建器 (context_builder)：

```Python
token_encoder = tiktoken.get_encoding("cl100k_base")
context_builder = GlobalCommunityContext(
    community_reports=reports,
    communities=communities,
    entities=entities,  
    token_encoder=token_encoder,
)
```

代码解释如下：

1. **`GlobalCommunityContext`**:
   1. 这是一个为 **Global Search** 模式创建的上下文构建器。它负责从不同的数据源（如社区报告、实体、社区信息等）中提取相关数据，并构建一个用于查询的大范围上下文。
   2. 这个构建器帮助为整个文档集合（而不是某个特定实体）构建一个全局的知识背景，以便模型能够对广泛的问题做出响应。
2. **`community_reports=reports`**:
   1. 这里传入的是之前从文件中读取的 `reports` 数据（也就是 `COMMUNITY_REPORT_TABLE` 表格的数据）。
   2. 这些报告包含了关于不同社区的详细信息，如主题、摘要、影响力、发现等。
   3. 在全局搜索中，这些社区报告有助于构建整个数据集的高层次概览。
3. **`communities=communities`**:
   1. `communities` 数据包含社区的结构和信息。在图谱中，社区可能代表了不同的主题、领域或相关性较高的实体群体。
   2. 这部分数据通常用于在全局搜索时进行分组和排名，比如通过社群的重要性或与查询的相关性来排序。
4. **`entities=entities`**:
   1. `entities` 是从之前的索引步骤中提取的实体数据（来自 `ENTITY_TABLE` 表）。
   2. 这些实体（如人物、地点、事件等）可以用来扩展全局搜索的范围。它们提供了具体的名词、对象和概念，有助于为全局查询提供上下文。
   3. **注意：** 如果不希望在全局搜索中使用社区权重来影响排名（例如，不考虑某个社区对某个实体的影响），可以将 `entities` 参数设为 `None`。
5. **`token_encoder=token_encoder`**:
   1. `token_encoder` 是用于对文本进行编码的工具。它将文本转化为可以输入到模型中的 token 序列，以便在模型中使用。

配置全局搜索参数（结合下面的“构建全局搜索引擎”使用）：

```Python
context_builder_params = {
    "use_community_summary": False,  
    "shuffle_data": True,
    "include_community_rank": True,
    "min_community_rank": 0,
    "community_rank_name": "rank",
    "include_community_weight": True,
    "community_weight_name": "occurrence weight",
    "normalize_community_weight": True,
    "max_tokens": 12_000,  
    "context_name": "Reports",
}

map_llm_params = {
    "max_tokens": 1000,
    "temperature": 0.0,
    "response_format": {"type": "json_object"},
}

reduce_llm_params = {
    "max_tokens": 2000, 
    "temperature": 0.0,
}
```

构建全局搜索引擎：

```Python
llm = ChatOpenAI(
    api_key="sk-4b79f3a3ff334a15a1935366ebb425b3",
    model="deepseek-chat",
    api_base="https://api.deepseek.com",
    api_type=OpenaiApiType.OpenAI,  
    max_retries=20,
)

search_engine = GlobalSearch(
    llm=llm,
    context_builder=context_builder,
    token_encoder=token_encoder,
    max_data_tokens=12_000,  
    map_llm_params=map_llm_params,
    reduce_llm_params=reduce_llm_params,
    allow_general_knowledge=False, 
    json_mode=True,  
    context_builder_params=context_builder_params,
    concurrent_coroutines=32,
    response_type="multiple paragraphs",  
)
```

这里创建了一个 **全局搜索（Global Search）** 引擎，利用前面配置的上下文构建器 (`context_builder`)、语言模型 (`llm`)、以及其它相关的参数进行搜索。对应参数详解如下：

- **`llm`**:
  - 这个参数传入的是已经配置好的语言模型（LLM）。全局搜索引擎将使用这个模型来生成回答。
- **`context_builder`**:
  - 上下文构建器，它负责根据社区报告、社区等信息来构建查询的上下文。
- **`token_encoder`**:
  - `token_encoder` 是用来处理文本的编码工具，通常是一个模型专用的 tokenizer。在这里，我们使用了 `tiktoken.get_encoding("cl100k_base")`，它是 OpenAI 模型的一个编码器，用来将文本转化为 token 格式。
- **`max_data_tokens`**:
  - 最大数据 token 数量。它控制了模型可以处理的最大上下文大小。你可以根据实际使用的模型的最大 token 限制来设置（例如，如果模型最大 token 限制是 8K，则可以设置为 5000，留一些余量）。这个设置控制了全局搜索时在上下文窗口内所使用的最大 token 数。
- **`map_llm_params`** 和 **`reduce_llm_params`**:
  - 这些参数会影响 LLM 在不同阶段生成内容的方式（例如，`max_tokens` 和 `temperature` 等）。
  - 在GraphRAG框架中，**`map_llm_params`（映射阶段）和`reduce_llm_params`（归约阶段）**代表了模型处理任务时的双向策略。在复杂图谱中，关键证据往往隐藏在非直觉性的间接连接里。只有充分展开搜索树才能确保不遗漏重要分支。通过这种分治策略，GraphRAG既能像蜘蛛网一样广泛感知环境变化，又能像激光般精准定位关键节点，在知识密集型任务中实现效率与准确性的平衡。
  - Map阶段对应发散思维过程，使用较宽松的温度系数鼓励多样化候选集生成；适用于头脑风暴式探索潜在关联路径。
  - Reduce阶段侧重收敛决策，采用低温度强化逻辑一致性；常用于冲突消解和最优解筛选。
- **`allow_general_knowledge`**:
  - 这个参数控制是否允许模型在回答中加入通用知识。如果设置为 `True`，LLM 会尝试将 **外部知识** 加入到查询的结果中。这对于需要广泛知识背景的任务可能有帮助，但也有可能导致模型生成 **虚假信息**（hallucinations）。为了避免这个问题，默认值设置为 `False`。
- **`json_mode`**:
  - 这个参数控制结果的格式。如果设置为 `True`，LLM 会生成结构化的 **JSON 格式** 输出。如果设置为 `False`，则返回的是更自由形式的文本回答。对于结构化数据的处理，通常使用 JSON 格式。
- **`context_builder_params`**:
  - 这是传入给上下文构建器的参数，用来进一步配置如何构建查询上下文（例如是否使用社区简要摘要、是否包含社区排名等）。
- **`concurrent_coroutines`**:
  - 这个参数控制并发协程的数量。全局搜索引擎支持并发处理多个查询，如果你需要同时处理多个请求，可以增加这个值。比如设置为 `32`，意味着最多可以同时处理 32 个查询。
- **`response_type`**:
  - 这个参数定义了模型生成的响应的类型和格式。它是一个自由文本的描述，指明返回的内容应该是什么样的格式。在这里，`"multiple paragraphs"` 表示模型会生成多段文字的回答，适合长篇的说明或报告。

执行全局搜索：

```Python
from IPython.display import display, Code, Markdown

result = await search_engine.asearch("请帮我介绍下什么是执剑人？")
display(Markdown(result.response))
```
