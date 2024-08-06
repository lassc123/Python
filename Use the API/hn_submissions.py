import requests
from operator import itemgetter  # 添加这一行
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# 创建会话并设置重试策略
session = requests.Session()
retry = Retry(
    total=5,
    backoff_factor=0.1,
    status_forcelist=[500, 502, 503, 504],
    raise_on_status=False
)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# 发出请求并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = session.get(url)
print("Status code:", r.status_code)

if r.status_code != 200:
    print("Failed to retrieve top stories.")
else:
    # 处理每篇文章的信息
    submission_ids = r.json()
    submission_dicts = []
    for submission_id in submission_ids[:30]:
        # 对每篇文章发出请求
        submission_url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
        try:
            submission_r = session.get(submission_url)
            print(submission_r.status_code)

            if submission_r.status_code == 200:
                try:
                    response_dict = submission_r.json()
                    submission_dict = {
                        'title': response_dict['title'],
                        'link': f'http://news.ycombinator.com/item?id={submission_id}',
                        'comments': response_dict.get('descendants', 0)
                    }
                    submission_dicts.append(submission_dict)
                except KeyError as e:
                    print(f"Missing expected field {e} in submission {submission_id}")
                except ValueError as e:
                    print(f"Error decoding JSON for submission {submission_id}: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed for submission {submission_id}: {e}")

    # 对结果进行排序
    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

    for submission_dict in submission_dicts:
        print("\nTitle:", submission_dict['title'])
        print("Discussion link:", submission_dict['link'])
        print("Comments:", submission_dict['comments'])
