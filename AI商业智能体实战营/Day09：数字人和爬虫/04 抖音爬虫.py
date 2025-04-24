# import requests
#
# url = "https://www-hj.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAQERLUS1XLl1qZMZDkibRWUdHGBAoG0pJq_5hAj3XjIZXnxgtW_CcE17nuHHfikpQ&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&from_user_page=1&update_version_code=170400&pc_client_type=1&pc_libra_divert=Mac&support_h265=1&support_dash=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1728&screen_height=1117&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=135.0.0.0&browser_online=true&engine_name=Blink&engine_version=135.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7290435875619390995&uifid=7457f5ef2178e63069f24974fa04cbf9321b3fa7afdb44208071bc08e7f7084f74363975da09c159decfeaaf0ebff3b1c996831f1f741be4c2b9be26c828e21f845d319e36e4d40936d08b5dba290a1df778ae803c4a52085dcc143abf08110c1ae5fc218bfb174f3a9e393f2a512f888b17a6d218e62f8a723d07d9fcf61fcf7efe06832a080c4ddd60975ffb1aca7e1fb0150798f30863ac2e4b879fb7273f&verifyFp=verify_m82lc1lh_KenlS6td_Uwum_47Ab_Au1K_kx5vD2USLgG6&fp=verify_m82lc1lh_KenlS6td_Uwum_47Ab_Au1K_kx5vD2USLgG6&msToken=xqw7_YH3BsQgmxd1cIFaSF-xco6okzkWlMqrBpv0Uuk1t2OUqLHCP3S3ILkU7JTiox71kLAn5DcxTuCmJEoM6RBfXPNOnZeACz4vXzdUDFJ6pXMOsN-2IieFWU2LFwog44Z1oHrIpEZidYE2S5JalZ5-RX2ia7PxgQ-zrbDIy9Mghzcj-mXA&a_bogus=EX05D76JYNQ5adFGuOEq71IUm02MrsWyiZTKRCCTHOK1GqMc68PHZPGGGowzfNhqzWpkieVHSDGlbVVc%2FGX0ZHrkumpkSBkWB055VwsogqqZTzvdDHfwSguFwwMSUbTFeQnfNAUR6s0j2DQ6VrCwAdcjo%2Flx-REDTN3JVZTaY2cm-AWcdJqKYoi1Ck3T-GA6sjy%3D"
# my_headers = {
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
#     "referer": "https://www.douyin.com/",
#     "cookie":"live_use_vvc=%22false%22; bd_ticket_guard_client_web_domain=2; store-region=cn-bj; store-region-src=uid; UIFID_TEMP=7457f5ef2178e63069f24974fa04cbf9321b3fa7afdb44208071bc08e7f7084f042f754fb251c16db9002c1f685798f27f973ee3bb34568db3855242c8f85befa4cc10028809e89e0a86550333f40359; UIFID=7457f5ef2178e63069f24974fa04cbf9321b3fa7afdb44208071bc08e7f7084f74363975da09c159decfeaaf0ebff3b1c996831f1f741be4c2b9be26c828e21f845d319e36e4d40936d08b5dba290a1df778ae803c4a52085dcc143abf08110c1ae5fc218bfb174f3a9e393f2a512f888b17a6d218e62f8a723d07d9fcf61fcf7efe06832a080c4ddd60975ffb1aca7e1fb0150798f30863ac2e4b879fb7273f; hevc_supported=true; d_ticket=5179eeffbd72449a30e5b3cc9a006334c2776; n_mh=k9zkCfOQfFegoa7kc0V7SXvDVdHwnUROJ967U1dUUI0; SelfTabRedDotControl=%5B%5D; __live_version__=%221.1.2.6953%22; passport_csrf_token=2b8d623222a99e8482575f0a2e42fc64; passport_csrf_token_default=2b8d623222a99e8482575f0a2e42fc64; __security_mc_1_s_sdk_crypt_sdk=f594d879-4f26-b693; __security_mc_1_s_sdk_cert_key=6e4563d2-466f-a4ec; __security_mc_1_s_sdk_sign_data_key_sso=b1ea5add-4398-91d0; passport_mfa_token=CjW5XhmLplmYCF1BJACZltEDnxRULCgTQEGt3IGKw0qxgQXwbACVIy6315SkOHu6fvjLLMOvDBpKCjyLPXOAHEk4NqxrCoFh%2Fw4u926Y4goDUGXlPT%2F3m8AT%2FL8W6Dd2bHmDl7O22sYsbAB1hXX4gM5fhwGe56MQpv7rDRj2sdFsIAIiAQO%2BL46m; __security_mc_1_s_sdk_sign_data_key_web_protect=f4a6b9d4-4fd5-b2c1; _bd_ticket_crypt_cookie=ae6240d42c86f07a27ed6b353e2331f0; my_rd=2; SearchMultiColumnLandingAbVer=1; SEARCH_RESULT_LIST_TYPE=%22multi%22; login_time=1744085348218; odin_tt=3a07c628002e7a3d918c8947b233bd3ab31b0868933a0b8a060982fcb882ccd407ec9aaba55dc0d29fca60815d73b5fd0b0a3d78d89327f047efc663eb0043848da76bf0575ad0f1e60a3e1b36568759; ttwid=1%7CvQ6QCiLyIG9SJypBIXRtIfGPJXv6br9a79NgmLfR-U4%7C1745141755%7Cbb214dc6e9c1c1bcf05e77a7f1ff0d8ea12b333372e65850f6679b8d8fb44436; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1728%2C%5C%22screen_height%5C%22%3A1117%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A10%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; strategyABtestKey=%221745315134.02%22; is_dash_user=1; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; WallpaperGuide=%7B%22showTime%22%3A1745316674873%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A10%2C%22cursor2%22%3A2%2C%22hoverTime%22%3A1745317867191%7D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.116%7D; biz_trace_id=04e7e15e; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e5827292771273f27333d373d323430363630313234272927676c715a75776a716a666a69273f2763646976602778; bit_env=FC2QVawFLijGOonZALBYTStnskDEBp8XPrp1pzqN0u6Tn-1JNIB9ThBicW5UKaWfUg-qjFDZHUIQ03z9Gufpg509dWqF8TYqIqt1oggVoF9ojzjXWzkRcpS13mcn2_bnNis-NY1Hj7NFM3TvrnFeCFCnS4qHw31izIK6mPrPfZMXQsvbCsJRKKHIa0ngtu2qZjnVmkXJ2lPyfQLia6nkOZR9TD-V2UWYtzFoo3AKVn0KXJk0uD7mesb1usLbKhq3EEZkdEL7qQfQZ9m-em0sPbmMHNKy7vnBupsoa8VyJsMQJtGXoYzadNke327kFUrhGg7FM_wG-jYlm8xBKnQNL1vRw8AG4dkU3sAmeQLR6K9u_Nco-e0VpRgp3-yLCF_TTdomB2w7FejbUddyX1HPGt18q50DnRFn0ajbCm2kmYqWQ-MF3B0AQEjfvmdtNJ8rkTW58Mw-fI5GSfyIsGDpiWvBt9BvNcfja2Z2gTsxvs2EFXLJwWpy7wUgSLTqhc8JS-jjB6ym6gD2NcLdRUZQX0huAD5T-phRnkxSEMp-77E%3D; gulu_source_res=eyJwX2luIjoiMmJkMzcyNDZkMGEwMTFjMWNhNDFlMmYwM2I3NTQzNTljZjlkMTExY2U3N2UxMTIxODgxNmNiNDg0N2Q1Y2FhNCJ9; passport_auth_mix_state=b53ur5whjw1il4l4kiynavilbybgly5p; SearchColumnSwitchLog=%5B%7B%22date%22%3A%222025-04-22%22%2C%22latestColumnType%22%3A%22multi%22%7D%5D; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; download_guide=%223%2F20250422%2F0%22; IsDouyinActive=true; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQnNtWm5qUEJ6SExwVlpzZjhzV1BoYWlOQzJZM0ZNNk9iTnNoOGRQMzFmRFVtOVdDLzhXWHJ4NVFDTXZvTWZLdFNuMVlKU2ZvclVETmZ6SEkrUkF5MVE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D"
#
# }
# res = requests.get(url, headers=my_headers)
# print(res.text)


import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'origin': 'https://www.douyin.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.douyin.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'uifid': '7457f5ef2178e63069f24974fa04cbf9321b3fa7afdb44208071bc08e7f7084f74363975da09c159decfeaaf0ebff3b1c996831f1f741be4c2b9be26c828e21f845d319e36e4d40936d08b5dba290a1df778ae803c4a52085dcc143abf08110c1ae5fc218bfb174f3a9e393f2a512f888b17a6d218e62f8a723d07d9fcf61fcf7efe06832a080c4ddd60975ffb1aca7e1fb0150798f30863ac2e4b879fb7273f',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'cookie': 'live_use_vvc=%22false%22; bd_ticket_guard_client_web_domain=2; store-region=cn-bj; store-region-src=uid; UIFID_TEMP=7457f5ef2178e63069f24974fa04cbf9321b3fa7afdb44208071bc08e7f7084f042f754fb251c16db9002c1f685798f27f973ee3bb34568db3855242c8f85befa4cc10028809e89e0a86550333f40359; UIFID=7457f5ef2178e63069f24974fa04cbf9321b3fa7afdb44208071bc08e7f7084f74363975da09c159decfeaaf0ebff3b1c996831f1f741be4c2b9be26c828e21f845d319e36e4d40936d08b5dba290a1df778ae803c4a52085dcc143abf08110c1ae5fc218bfb174f3a9e393f2a512f888b17a6d218e62f8a723d07d9fcf61fcf7efe06832a080c4ddd60975ffb1aca7e1fb0150798f30863ac2e4b879fb7273f; hevc_supported=true; d_ticket=5179eeffbd72449a30e5b3cc9a006334c2776; n_mh=k9zkCfOQfFegoa7kc0V7SXvDVdHwnUROJ967U1dUUI0; SelfTabRedDotControl=%5B%5D; __live_version__=%221.1.2.6953%22; passport_csrf_token=2b8d623222a99e8482575f0a2e42fc64; passport_csrf_token_default=2b8d623222a99e8482575f0a2e42fc64; __security_mc_1_s_sdk_crypt_sdk=f594d879-4f26-b693; __security_mc_1_s_sdk_cert_key=6e4563d2-466f-a4ec; __security_mc_1_s_sdk_sign_data_key_sso=b1ea5add-4398-91d0; passport_mfa_token=CjW5XhmLplmYCF1BJACZltEDnxRULCgTQEGt3IGKw0qxgQXwbACVIy6315SkOHu6fvjLLMOvDBpKCjyLPXOAHEk4NqxrCoFh%2Fw4u926Y4goDUGXlPT%2F3m8AT%2FL8W6Dd2bHmDl7O22sYsbAB1hXX4gM5fhwGe56MQpv7rDRj2sdFsIAIiAQO%2BL46m; __security_mc_1_s_sdk_sign_data_key_web_protect=f4a6b9d4-4fd5-b2c1; _bd_ticket_crypt_cookie=ae6240d42c86f07a27ed6b353e2331f0; my_rd=2; SearchMultiColumnLandingAbVer=1; SEARCH_RESULT_LIST_TYPE=%22multi%22; login_time=1744085348218; odin_tt=3a07c628002e7a3d918c8947b233bd3ab31b0868933a0b8a060982fcb882ccd407ec9aaba55dc0d29fca60815d73b5fd0b0a3d78d89327f047efc663eb0043848da76bf0575ad0f1e60a3e1b36568759; ttwid=1%7CvQ6QCiLyIG9SJypBIXRtIfGPJXv6br9a79NgmLfR-U4%7C1745141755%7Cbb214dc6e9c1c1bcf05e77a7f1ff0d8ea12b333372e65850f6679b8d8fb44436; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1728%2C%5C%22screen_height%5C%22%3A1117%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A10%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; strategyABtestKey=%221745315134.02%22; is_dash_user=1; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; WallpaperGuide=%7B%22showTime%22%3A1745316674873%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A10%2C%22cursor2%22%3A2%2C%22hoverTime%22%3A1745317867191%7D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.116%7D; biz_trace_id=04e7e15e; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e5827292771273f27333d373d323430363630313234272927676c715a75776a716a666a69273f2763646976602778; bit_env=FC2QVawFLijGOonZALBYTStnskDEBp8XPrp1pzqN0u6Tn-1JNIB9ThBicW5UKaWfUg-qjFDZHUIQ03z9Gufpg509dWqF8TYqIqt1oggVoF9ojzjXWzkRcpS13mcn2_bnNis-NY1Hj7NFM3TvrnFeCFCnS4qHw31izIK6mPrPfZMXQsvbCsJRKKHIa0ngtu2qZjnVmkXJ2lPyfQLia6nkOZR9TD-V2UWYtzFoo3AKVn0KXJk0uD7mesb1usLbKhq3EEZkdEL7qQfQZ9m-em0sPbmMHNKy7vnBupsoa8VyJsMQJtGXoYzadNke327kFUrhGg7FM_wG-jYlm8xBKnQNL1vRw8AG4dkU3sAmeQLR6K9u_Nco-e0VpRgp3-yLCF_TTdomB2w7FejbUddyX1HPGt18q50DnRFn0ajbCm2kmYqWQ-MF3B0AQEjfvmdtNJ8rkTW58Mw-fI5GSfyIsGDpiWvBt9BvNcfja2Z2gTsxvs2EFXLJwWpy7wUgSLTqhc8JS-jjB6ym6gD2NcLdRUZQX0huAD5T-phRnkxSEMp-77E%3D; gulu_source_res=eyJwX2luIjoiMmJkMzcyNDZkMGEwMTFjMWNhNDFlMmYwM2I3NTQzNTljZjlkMTExY2U3N2UxMTIxODgxNmNiNDg0N2Q1Y2FhNCJ9; passport_auth_mix_state=b53ur5whjw1il4l4kiynavilbybgly5p; SearchColumnSwitchLog=%5B%7B%22date%22%3A%222025-04-22%22%2C%22latestColumnType%22%3A%22multi%22%7D%5D; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; download_guide=%223%2F20250422%2F0%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQnNtWm5qUEJ6SExwVlpzZjhzV1BoYWlOQzJZM0ZNNk9iTnNoOGRQMzFmRFVtOVdDLzhXWHJ4NVFDTXZvTWZLdFNuMVlKU2ZvclVETmZ6SEkrUkF5MVE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22',
}

params = {
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'sec_user_id': 'MS4wLjABAAAAQERLUS1XLl1qZMZDkibRWUdHGBAoG0pJq_5hAj3XjIZXnxgtW_CcE17nuHHfikpQ',
    'max_cursor': '0',
    'locate_query': 'false',
    'show_live_replay_strategy': '1',
    'need_time_list': '1',
    'time_list_query': '0',
    'whale_cut_token': '',
    'cut_version': '1',
    'count': '18',
    'publish_video_strategy_type': '2',
    'from_user_page': '1',
    'update_version_code': '170400',
    'pc_client_type': '1',
    'pc_libra_divert': 'Mac',
    'support_h265': '1',
    'support_dash': '1',
    'version_code': '290100',
    'version_name': '29.1.0',
    'cookie_enabled': 'true',
    'screen_width': '1728',
    'screen_height': '1117',
    'browser_language': 'zh-CN',
    'browser_platform': 'MacIntel',
    'browser_name': 'Chrome',
    'browser_version': '135.0.0.0',
    'browser_online': 'true',
    'engine_name': 'Blink',
    'engine_version': '135.0.0.0',
    'os_name': 'Mac OS',
    'os_version': '10.15.7',
    'cpu_core_num': '10',
    'device_memory': '8',
    'platform': 'PC',
    'downlink': '10',
    'effective_type': '4g',
    'round_trip_time': '50',
    'webid': '7290435875619390995',
    'uifid': '7457f5ef2178e63069f24974fa04cbf9321b3fa7afdb44208071bc08e7f7084f74363975da09c159decfeaaf0ebff3b1c996831f1f741be4c2b9be26c828e21f845d319e36e4d40936d08b5dba290a1df778ae803c4a52085dcc143abf08110c1ae5fc218bfb174f3a9e393f2a512f888b17a6d218e62f8a723d07d9fcf61fcf7efe06832a080c4ddd60975ffb1aca7e1fb0150798f30863ac2e4b879fb7273f',
    'verifyFp': 'verify_m82lc1lh_KenlS6td_Uwum_47Ab_Au1K_kx5vD2USLgG6',
    'fp': 'verify_m82lc1lh_KenlS6td_Uwum_47Ab_Au1K_kx5vD2USLgG6',
    'msToken': 'IlsC3mwiBH6wuD1nB_kKMYfyMGoADLYvZNnDXhzLqPtmA6oYN4s22j15oYzfAkiMGz3w-qCnZZs8d31XZTQuOcc-VfJtNfeZrbkiXniN5iGLBFLXAwNqcD7nO2lsKyB4GIus38ryFY4vY2utWuCdA0jX3RdWWW_XNcvQe3PJaTukmLdR4fBI',
    'a_bogus': 'xy0nkttLDo8VPdFGYKajHceUsh2ANB8y1NidbqMTyNORThFcxuN1qNSGaoqG4Ny7sRBiieIHKnt/bDnc/GX0Z9HpzmkfuPJWMUV5VLsL0qq2TzidLqfpC0DFFwMzU5TFaAnjNIRR6sMJ2x56IrCwApCjw/UN-RfD0q3JV/uai2bsBSucd7q/YKw1Hk3Y--K6sHS=',
}

url = "https://www-hj.douyin.com/aweme/v1/web/aweme/post/"
response = requests.get(url, params=params, headers=headers)

aweme_list = response.json().get("aweme_list")

for aweme in aweme_list:
    desc = aweme.get("desc")
    url = aweme.get("video").get("play_addr").get("url_list")[-1]
    # 爬虫一个短视频
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'i',
        'range': 'bytes=0-',
        'referer': 'https://v95-zjb-a.douyinvod.com/4a6dc8117794abe976b81ffe4aba0130/6807c58b/video/tos/cn/tos-cn-ve-15c001-alinc2/oYZGiK8ig6eLQEhIoBi0A5QBghCLBAO9f2AAi2/?a=1128&ch=0&cr=0&dr=0&er=0&cd=0%7C0%7C0%7C0&cv=1&br=1046&bt=1046&cs=0&ds=4&ft=VJbLr3TIRR0sWrC12D12Nc.xBiGNbLlb19dU_4n3eTxJNv7TGW&mime_type=video_mp4&qs=0&rc=M2dnaWQ8OWc4Z2k0M2Q4NUBpanNoaHA5cmtnMzMzNGkzM0A2MGEtNDU1XjQxYC5iMzQwYSNkMWUyMmRjcDBhLS1kLS9zcw%3D%3D&btag=c0000e0008d200&cquery=100y&dy_q=1745336176&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=202504222336169B618D1EA3F42931502F',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'video',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    }

    params = {
        'a': '1128',
        'ch': '0',
        'cr': '0',
        'dr': '0',
        'er': '0',
        'cd': '0|0|0|0',
        'cv': '1',
        'br': '1046',
        'bt': '1046',
        'cs': '0',
        'ds': '4',
        'ft': 'VJbLr3TIRR0sWrC12D12Nc.xBiGNbLlb19dU_4n3eTxJNv7TGW',
        'mime_type': 'video_mp4',
        'qs': '0',
        'rc': 'M2dnaWQ8OWc4Z2k0M2Q4NUBpanNoaHA5cmtnMzMzNGkzM0A2MGEtNDU1XjQxYC5iMzQwYSNkMWUyMmRjcDBhLS1kLS9zcw==',
        'btag': 'c0000e0008d200',
        'cquery': '100y',
        'dy_q': '1745336176',
        'feature_id': '46a7bb47b4fd1280f3d3825bf2b29388',
        'l': '202504222336169B618D1EA3F42931502F',
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
    )

    # print(response.content)

    # 将数据写入一个

    with open(f"./videos/{desc}.mp4", "wb") as f:
        f.write(response.content)

    print(f"{desc}下载成功")
