# -*- coding: utf-8 -*-
import json
import re
from datetime import datetime
import numpy as np
import pandas as pd
import requests
from flask import Flask, request, jsonify, render_template


app = Flask(__name__) 
  
# The route() function of the Flask class is a decorator,  
# which tells the application which URL should call  
# the associated function. 
@app.route('/', methods= ["GET"]) 
# ‘/’ URL is bound with hello_world() function. 
def query_news():
    news_item = []

    df = pd.DataFrame(columns=['title', 'publish_time', 'media_name','url','description','picurl'])

    # Part 1: Scraping information from websites

    # -----------------------Bing (China)-----------------------
    url = "https://bing-news-search1.p.rapidapi.com/news/search"
    querystring = {"cc":"CN","freshness":"Month","textFormat":"Raw","safeSearch":"Off","q":"中集集团"}
    headers = {
        'x-rapidapi-host': "bing-news-search1.p.rapidapi.com",
        'x-rapidapi-key': "adb27ffe06msh96b2001e85b3808p15f555jsn560ce40bd0cf",
        'x-bingapis-sdk': "true"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response.raise_for_status()
    response = response.text
    response = json.loads(response)
    data_list = response.get('value')
    for data in data_list:
        title = data.get('name')
        if title not in news_item:
            if (data.get('image')):
                picurl = data.get('image').get('thumbnail').get('contentUrl')
            else:
                picurl = 'https://www.cimc.com/en/uploadfile/2016/0308/20160308114409462.jpg'
            df = df.append({ "title": data.get('name').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""), 
                            "publish_time": data.get('datePublished').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "media_name": data.get('provider')[0].get('name'),
                            'url': data.get('url').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "description": data.get('description').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "picurl": picurl
                    }, ignore_index=True)
            news_item.append(title)

    # -----------------------Bing (China)-----------------------
    url = "https://bing-news-search1.p.rapidapi.com/news/search"
    querystring = {"cc":"CN","freshness":"Month", "textFormat":"Raw","safeSearch":"Off","q":"中集"}
    headers = {
        'x-rapidapi-host': "bing-news-search1.p.rapidapi.com",
        'x-rapidapi-key': "adb27ffe06msh96b2001e85b3808p15f555jsn560ce40bd0cf",
        'x-bingapis-sdk': "true"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response.raise_for_status()
    response = response.text
    response = json.loads(response)
    data_list = response.get('value')
    for data in data_list:
        title = data.get('name')
        if title not in news_item:
            if (data.get('image')):
                picurl = data.get('image').get('thumbnail').get('contentUrl')
            else:
                picurl = 'https://www.cimc.com/en/uploadfile/2016/0308/20160308114409462.jpg'
            df = df.append({ "title": data.get('name').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""), 
                            "publish_time": data.get('datePublished').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "media_name": data.get('provider')[0].get('name'),
                            'url': data.get('url').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "description": data.get('description').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "picurl": picurl
                    }, ignore_index=True)
            news_item.append(title)
    

    # -----------------------Bing (US)-----------------------
    url = "https://bing-news-search1.p.rapidapi.com/news/search"

    querystring = {"count":"32","cc":"US","freshness":"Month","textFormat":"Raw","safeSearch":"Off","q":"China International Marine Containers"}

    headers = {
        'x-rapidapi-host': "bing-news-search1.p.rapidapi.com",
        'x-rapidapi-key': "adb27ffe06msh96b2001e85b3808p15f555jsn560ce40bd0cf",
        'x-bingapis-sdk': "true"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response.raise_for_status()
    response = response.text
    response = json.loads(response)
    data_list = response.get('value')
    for data in data_list:
        title = data.get('name')
        if title not in news_item:
            if (data.get('image')):
                picurl = data.get('image').get('thumbnail').get('contentUrl')
            else:
                picurl = 'https://www.cimc.com/en/uploadfile/2016/0308/20160308114409462.jpg'
            df = df.append({ "title": data.get('name').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""), 
                            "publish_time": data.get('datePublished').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "media_name": data.get('provider')[0].get('name'),
                            'url': data.get('url').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "description": data.get('description').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "picurl": picurl
                    }, ignore_index=True)
            news_item.append(title)

    # -----------------------Toutiao (China)-----------------------
    url = 'http://api.tianapi.com/topnews/index?key=f792509ff8339f62329519465dcce0e7'
    querystring = {"word": "中集集团"}
    response = requests.request("GET", url, params=querystring)
    response.raise_for_status()
    response = response.text
    response = json.loads(response)
    data_list = response.get('newslist')
    if data_list != None:
        if data not in data_list:
            title = data.get('title')
            if (title == None):
                title = "无"
            else:
                title = title.replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", "")
            
            time = data.get('ctime')
            if (time == None):
                time = "无"
            else:
                time = time.replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", "")

            media_name = data.get('source')
            if (media_name == None):
                media_name = "无"
            else:
                media_name = media_name.replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", "")

            url = data.get('url')
            if (url == None):
                url = "无"
            else:
                url = media_name.replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", "")

            description = data.get('description')
            if (description == None):
                description = "无"
            else:
                description = description.replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", "")

            if title not in news_item:
                df = df.append({ "title": title, 
                                    "publish_time": time,
                                    "media_name": media_name,
                                    'url': url,
                                    "description": description,
                                    'picUrl': 'https://www.cimc.com/en/uploadfile/2016/0308/20160308114409462.jpg'
                            }, ignore_index=True)
                news_item.append(title)

     # -----------------------Domestic News (China)-----------------------
    url = "http://api.tianapi.com/generalnews/index?key=f792509ff8339f62329519465dcce0e7"
    querystring = {"word": "中集集团"}
    response = requests.request("GET", url, params=querystring)
    response.raise_for_status()
    response = response.text
    response = json.loads(response)
    data_list = response.get('newslist')
    if data_list != None:
        for data in data_list:
            title = data.get('name')
            if title not in news_item:
                df = df.append({ "title": data.get('title').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""), 
                                "publish_time": data.get('ctime').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                                "media_name": data.get('description'),
                                'url': data.get('url').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                                "description": data.get('description').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                                "picUrl": data.get('picUrl').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", "")
                        }, ignore_index=True)
                news_item.append(title)




    # # Part 2: Data cleaning
    df = df[df['url'] != "无"]

    df['publish_time'] = df['publish_time'].str.slice(stop=10)

    df.sort_values(by=['publish_time'], inplace=True, ascending=False)

    # debugging purpose
    # writer = pd.ExcelWriter('output.xlsx')

    # df.to_excel(writer, 'marks')

    # writer.save()
    # print('DataFrame is written successfully to Excel Sheet.')

    # Part 3: Changing to Json format

    # df = pd.read_excel('output.xlsx')

    df_json = df.to_json(orient='records')

    jsonfiles = df_json

    return jsonfiles

@app.route('/', methods= ["POST"]) 
# ‘/’ URL is bound with hello_world() function. 
def post_query_news():
    news_item = []

    data = request.get_json()
    keyword = data['data']

    df = pd.DataFrame(columns=['title', 'publish_time', 'media_name','url','description','picurl'])

    # Part 1: Scraping information from websites

    # -----------------------Bing (China)-----------------------
    url = "https://bing-news-search1.p.rapidapi.com/news/search"
    querystring = {"cc":"CN","textFormat":"Raw","safeSearch":"Off","q":keyword}
    headers = {
        'x-rapidapi-host': "bing-news-search1.p.rapidapi.com",
        'x-rapidapi-key': "adb27ffe06msh96b2001e85b3808p15f555jsn560ce40bd0cf",
        'x-bingapis-sdk': "true"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response.raise_for_status()
    response = response.text
    response = json.loads(response)
    data_list = response.get('value')
    for data in data_list:
        title = data.get('name')
        if title not in news_item:
            if (data.get('image')):
                picurl = data.get('image').get('thumbnail').get('contentUrl')
            else:
                picurl = 'https://www.cimc.com/en/uploadfile/2016/0308/20160308114409462.jpg'
            df = df.append({ "title": data.get('name').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""), 
                            "publish_time": data.get('datePublished').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "media_name": data.get('provider')[0].get('name'),
                            'url': data.get('url').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "description": data.get('description').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "picurl": picurl
                    }, ignore_index=True)
            news_item.append(title)

    # -----------------------Bing (China)-----------------------
    url = "https://bing-news-search1.p.rapidapi.com/news/search"
    querystring = {"cc":"CN","freshness":"Month", "textFormat":"Raw","safeSearch":"Off","q":keyword}
    headers = {
        'x-rapidapi-host': "bing-news-search1.p.rapidapi.com",
        'x-rapidapi-key': "adb27ffe06msh96b2001e85b3808p15f555jsn560ce40bd0cf",
        'x-bingapis-sdk': "true"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response.raise_for_status()
    response = response.text
    response = json.loads(response)
    data_list = response.get('value')
    for data in data_list:
        title = data.get('name')
        if title not in news_item:
            if (data.get('image')):
                picurl = data.get('image').get('thumbnail').get('contentUrl')
            else:
                picurl = 'https://www.cimc.com/en/uploadfile/2016/0308/20160308114409462.jpg'
            df = df.append({ "title": data.get('name').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""), 
                            "publish_time": data.get('datePublished').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "media_name": data.get('provider')[0].get('name'),
                            'url': data.get('url').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "description": data.get('description').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "picurl": picurl
                    }, ignore_index=True)
            news_item.append(title)
    

    # -----------------------Bing (US)-----------------------
    url = "https://bing-news-search1.p.rapidapi.com/news/search"

    querystring = {"cc":"US","freshness":"Month","textFormat":"Raw","safeSearch":"Off","q":keyword}

    headers = {
        'x-rapidapi-host': "bing-news-search1.p.rapidapi.com",
        'x-rapidapi-key': "adb27ffe06msh96b2001e85b3808p15f555jsn560ce40bd0cf",
        'x-bingapis-sdk': "true"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response.raise_for_status()
    response = response.text
    response = json.loads(response)
    data_list = response.get('value')
    for data in data_list:
        title = data.get('name')
        if title not in news_item:
            if (data.get('image')):
                picurl = data.get('image').get('thumbnail').get('contentUrl')
            else:
                picurl = 'https://www.cimc.com/en/uploadfile/2016/0308/20160308114409462.jpg'
            df = df.append({ "title": data.get('name').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""), 
                            "publish_time": data.get('datePublished').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "media_name": data.get('provider')[0].get('name'),
                            'url': data.get('url').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "description": data.get('description').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                            "picurl": picurl
                    }, ignore_index=True)
            news_item.append(title)

    # -----------------------Toutiao (China)-----------------------
    url = 'http://api.tianapi.com/topnews/index?key=f792509ff8339f62329519465dcce0e7'
    querystring = {"word": keyword}
    response = requests.request("GET", url, params=querystring)
    response.raise_for_status()
    response = response.text
    response = json.loads(response)
    data_list = response.get('newslist')
    if data_list != None:
        if data not in data_list:
            title = data.get('title')
            if (title == None):
                title = "无"
            else:
                title = title.replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", "")
            
            time = data.get('ctime')
            if (time == None):
                time = "无"
            else:
                time = time.replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", "")

            media_name = data.get('source')
            if (media_name == None):
                media_name = "无"
            else:
                media_name = media_name.replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", "")

            url = data.get('url')
            if (url == None):
                url = "无"
            else:
                url = media_name.replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", "")

            description = data.get('description')
            if (description == None):
                description = "无"
            else:
                description = description.replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", "")

            if title not in news_item:
                df = df.append({ "title": title, 
                                    "publish_time": time,
                                    "media_name": media_name,
                                    'url': url,
                                    "description": description,
                                    'picUrl': 'https://www.cimc.com/en/uploadfile/2016/0308/20160308114409462.jpg'
                            }, ignore_index=True)
                news_item.append(title)

     # -----------------------Domestic News (China)-----------------------
    url = "http://api.tianapi.com/generalnews/index?key=f792509ff8339f62329519465dcce0e7"
    querystring = {"word": keyword}
    response = requests.request("GET", url, params=querystring)
    response.raise_for_status()
    response = response.text
    response = json.loads(response)
    data_list = response.get('newslist')
    if data_list != None:
        for data in data_list:
            title = data.get('name')
            if title not in news_item:
                if (data.get('picUrl')):
                    picurl = data.get('picUrl').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", "")
                else:
                    picurl = 'https://www.cimc.com/en/uploadfile/2016/0308/20160308114409462.jpg'
                df = df.append({ "title": data.get('title').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""), 
                                "publish_time": data.get('ctime').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                                "media_name": data.get('description'),
                                'url': data.get('url').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                                "description": data.get('description').replace("\n", "").replace("<ul>", "").replace("<li>", "").replace("</li>", "").replace("</ul>", ""),
                                "picUrl": picurl
                        }, ignore_index=True)
                news_item.append(title)




    # # Part 2: Data cleaning
    df = df[df['url'] != "无"]

    df['publish_time'] = df['publish_time'].str.slice(stop=10)

    # df =df[df['description'].str.contains(keyword)]

    df.sort_values(by=['publish_time'], inplace=True, ascending=False)

    # debugging purpose
    # writer = pd.ExcelWriter('output.xlsx')

    # df.to_excel(writer, 'marks')

    # print(df)

    # writer.save()
    # print('DataFrame is written successfully to Excel Sheet.')

    # Part 3: Changing to Json format

    # df = pd.read_excel('output.xlsx')

    df_json = df.to_json(orient='records')

    jsonfiles = df_json

    return jsonfiles

   

  
# main driver function 
if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run() 
