data =  {
  "result": {
    "links": [
      {
        "description": "FisherAI (Alt + H)",
        "href": "https://fisherdaddy.com/",
        "title": "FisherAI"
      },
      {
        "description": "Archive",
        "href": "https://fisherdaddy.com/archives",
        "title": "Archive"
      },
      {
        "description": "Search (Alt + /)",
        "href": "https://fisherdaddy.com/search/",
        "title": "Search"
      },
      {
        "description": "Tags",
        "href": "https://fisherdaddy.com/tags/",
        "title": "Tags"
      },
      {
        "description": "AIBox",
        "href": "https://fishersama.com",
        "title": "AIBox"
      },
      {
        "description": "FisherAI.app",
        "href": "https://chromewebstore.google.com/detail/fisherai-your-best-summar/ipfiijaobcenaibdpaacbbpbjefgekbj",
        "title": "FisherAI.app"
      },
      {
        "description": "About",
        "href": "https://fisherdaddy.com/about/",
        "title": "About"
      },
      {
        "description": "",
        "href": "https://fisherdaddy.com/posts/introduce-ai-agent/",
        "title": ""
      },
      {
        "description": "",
        "href": "https://fisherdaddy.com/posts/react-reasoning-acting-language-models/",
        "title": ""
      },
      {
        "description": "",
        "href": "https://fisherdaddy.com/posts/how-to-think-about-agent-frameworks/",
        "title": ""
      },
      {
        "description": "",
        "href": "https://fisherdaddy.com/posts/the-second-half/",
        "title": ""
      },
      {
        "description": "",
        "href": "https://fisherdaddy.com/posts/iterative-approach-genai-evals/",
        "title": ""
      },
      {
        "description": "",
        "href": "https://fisherdaddy.com/posts/introducing-o3-and-o4-mini/",
        "title": ""
      },
      {
        "description": "",
        "href": "https://fisherdaddy.com/posts/introducing-gpt-4-1-models/",
        "title": ""
      },
      {
        "description": "",
        "href": "https://fisherdaddy.com/posts/llama-4-performance-controversy-analysis/",
        "title": ""
      },
      {
        "description": "",
        "href": "https://fisherdaddy.com/posts/how-llms-flip-the-script-on-technology-diffusion/",
        "title": ""
      },
      {
        "description": "",
        "href": "https://fisherdaddy.com/posts/ai-usage-is-now-a-baseline-expectation/",
        "title": ""
      },
      {
        "description": "",
        "href": "https://fisherdaddy.com/page/2/",
        "title": "Next 2/22 »"
      },
      {
        "description": "",
        "href": "https://fisherdaddy.com/",
        "title": "FisherAI"
      },
      {
        "description": "",
        "href": "https://gohugo.io/",
        "title": "Hugo"
      },
      {
        "description": "",
        "href": "https://github.com/adityatelange/hugo-PaperMod/",
        "title": "PaperMod"
      },
      {
        "description": "Privacy Policy",
        "href": "https://fisherdaddy.com/privacy/",
        "title": "Privacy Policy"
      },
      {
        "description": "Go to Top (Alt + G)",
        "href": "https://fisherdaddy.com/#top",
        "title": ""
      }
    ]
  }
}


ret = []
for item in data.get("result").get("links"):
    # print(item.get("href"))

    if item.get("href").find("https://fisherdaddy.com/posts") != -1:
        ret.append(item.get("href"))

print(ret)