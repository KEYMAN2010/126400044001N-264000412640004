from flask import Flask, request, jsonify

import asyncio

from aiohttp import ClientSession

import urllib.parse

import requests

import json

import time

import binascii

import re

from bs4 import BeautifulSoup

import base64

app = Flask(__name__)


@app.route('/')

def id():

    data = {

        'delta': "/delta/?link=Link&api_key=",

        'rekonise': "/rekonise/?link=Link&api_key=",

        'mboost': "/mboost/?link=Link&api_key=",

        'cokkahub': "/cokkahub/?link=Link&api_key=",

        'relzhub': "/relzhub/?link=Link&api_key="

    }

    return jsonify(data)

@app.route('/delta/', methods=['GET'])

def delta():

    link = request.args.get('link')


    if not link:

        return jsonify({"error": "No link"}), 400


    if link.startswith("https://gateway.platoboost.com/a/8?id="):

        id = link.replace("https://gateway.platoboost.com/a/8?id=", "")

        url_auth = f"https://api-gateway.platoboost.com/v1/sessions/auth/8/{id}"

    else:

        return jsonify({"error": "the url not vaild"}), 400

    start_time = time.time()

    try:

        r_auth = requests.post(url_auth)

        response_data = r_auth.json()

    except requests.RequestException as e:

        return jsonify({"error": f"Error Maybe Website Down: {str(e)}"}), 500

    except json.JSONDecodeError as e:

        return jsonify({"error": f"Failed to decode: {str(e)}"}), 500

    url = response_data.get("redirect")

    if not url:

        return jsonify({"error": "400 ERROR"}), 400

    prefix = "https://loot-link.com/s?fJjn&r="

    if url.startswith(prefix):

        hwid_encoded = url[len(prefix):]

        hwid_utf8 = urllib.parse.unquote(hwid_encoded)

        try:

            hwid_base64_decoded = base64.b64decode(hwid_utf8).decode('utf-8')

            token_match = re.search(r"&tk=(\w{4})", hwid_base64_decoded)

            if token_match:

                api_token = token_match.group(1)

                

                session = requests.Session()

                user_hwid = id 

                time.sleep(5)

                

                put_url = f"https://api-gateway.platoboost.com/v1/sessions/auth/8/{user_hwid}/{api_token}"

                try:

                    session.put(put_url)

                except requests.RequestException as e:

                    return jsonify({"error": f"request failed: {str(e)}"}), 500

                get_url = f"https://api-gateway.platoboost.com/v1/authenticators/8/{user_hwid}"

                try:

                    response_get = session.get(get_url)

                    response_get_data = response_get.json()

                    keybypassed = response_get_data.get("key", "No key found in response")

                except requests.RequestException as e:

                    return jsonify({"error": f" request failed: {str(e)}"}), 500

                except json.JSONDecodeError as e:

                    return jsonify({"error": f"Failed: {str(e)}"}), 500

                end_time = time.time()

                data = {

                    "key": keybypassed, 

                    "discord": "https://discord.com/invite/HvvsbpVz7d",

                    "credits": "Made by xpython01 and faisal8754",

                    "time_taken": round(end_time - start_time, 2) 

                }

                return jsonify(data), 200

            else:

                return jsonify({"error": "Failed 400"}), 400

        except (UnicodeDecodeError, binascii.Error) as e:

            return jsonify({"error": f"Failed :{str(e)}."}), 500

    else:

        return jsonify({"error": "Failed, Invalid URL"}), 400

@app.route('/rekonise/', methods=['GET'])

def rekonise():

    link = request.args.get('link')

    

    

    if not link:

        return jsonify({"success": False, "error": "No link provided"}), 400

    

            

    if link.startswith("https://rekonise.com"):

        hwid = link.replace("https://rekonise.com", "")

        start_time = time.time()

        api_url = f"https://api.rekonise.com/social-unlocks{hwid}"

        

        api = requests.get(api_url)

        

        if api.status_code == 200:

            data = api.json()

            url = data.get("url")

            if url:

                end_time = time.time()

                data = {

                    "url": url,

                    "credits": "Made by xpython01 and faisal8754",

                    "time_taken": round(end_time - start_time, 2)

                }

                return jsonify(data), 200

            else:

                return jsonify({"success": False, "error": "No URL found"}), 400

        else:

            return jsonify({"success": False, "error": "Invalid URL"}), 400

    else:

        return jsonify({"success": False, "error": "Link not valid"}), 400

@app.route('/cokkahub/', methods=['GET'])

def bypass():

    link = request.args.get('link')

    
    if not link or '=' not in link:

        return jsonify({"error": "Invalid URL parameter"}), 400

    

        

    user_id = link.split('=')[1]

    url_auth = f"https://api-gateway.platoboost.com/v1/sessions/auth/54658/{user_id}"

    start_time = time.time()

    try:

        post = requests.post(url_auth)

        post.raise_for_status()

        json_data = post.json()

        redirect_url = json_data.get("redirect", "")

        

        if "r=" not in redirect_url:

            return jsonify({"error": "Invalid redirect URL"}), 400

        hwid = redirect_url.split("r=")[1]

        hwid_utf8 = urllib.parse.unquote(hwid)

        hwid_base64_decoded = base64.b64decode(hwid_utf8).decode('utf-8')

        r819 = requests.get(hwid_base64_decoded, allow_redirects=True)

        final_url = r819.url

        token_match = re.search(r"&tk=(\w{4})", final_url)

        if token_match:

            api_token = token_match.group(1)

            session = requests.Session()

            time.sleep(5)

            put_url = f"https://api-gateway.platoboost.com/v1/sessions/auth/54658/{user_id}/{api_token}"

            session.put(put_url)

            get_url = f"https://api-gateway.platoboost.com/v1/authenticators/54658/{user_id}"

            response_get = session.get(get_url)

            response_get.raise_for_status()

            response_data = response_get.json()

            key_bypassed = response_data.get("key", "No key found. Please check your link")

            end_time = time.time()

            data = {

                "key": key_bypassed,

                "discord": "https://discord.gg/HvvsbpVz7d",

                "credits": "Made by xpython01 and faisal8754",

                "time_taken": round(end_time - start_time, 2)

            }

            return jsonify(data), 200

            

        else:

            return jsonify({"error": "Our Api Failed To Bypass Your link"}), 400

    except requests.RequestException as e:

        return jsonify({"error": f"Request failed"}), 500

@app.route('/mboost/')

def mboost():

    link = request.args.get('link')

    

    if not link:

        return jsonify({"result": "No URL provided."})

    

    try:

        response = requests.get(link)

        html_content = response.text

    except requests.RequestException:

        return jsonify({"result": "Failed to fetch the URL."})

    targeturl_regex = r'"targeturl":\s*"(.*?)"'

    match = re.search(targeturl_regex, html_content, re.MULTILINE)

    start_tim = time.time()

    if match and len(match.groups()) > 0:

        result = match.group(1)

        end_time = time.time()

        data = {

            "result": result,

            "discord": "https://discord.gg/HvvsbpVz7d",

            "credits": "Made by xpython01 and faisal8754",

            "time_taken": round(end_time - start_tim, 2)

        }

        return jsonify(data), 200

    else:

        return jsonify({"result": "Please try again later"})

relzheaders = {

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',

    'Accept-Language': 'en-US,en;q=0.5',

    'DNT': '1',

    'Connection': 'close',

    'Referer': 'https://linkvertise.com'

}

relz_key_pattern = r'const\s+keyValue\s*=\s*"([^"]+)"'

async def get_content(url, session):

    async with session.get(url, headers=relzheaders, allow_redirects=True) as response:

        html_text = await response.text()

        return html_text

async def fetch_key_value(link):

    urls = [

        link,

        'https://getkey.relzscript.xyz/check1.php',

        'https://getkey.relzscript.xyz/check2.php',

        'https://getkey.relzscript.xyz/check3.php',

        'https://getkey.relzscript.xyz/finished.php'

    ]

    async with ClientSession() as session:

        for url in urls:

            html_text = await get_content(url, session)

            soup = BeautifulSoup(html_text, 'html.parser')

            script_tags = soup.find_all('script')

            for script_tag in script_tags:

                script_content = script_tag.string

                if script_content:

                    key_match = re.search(relz_key_pattern, script_content)

                    if key_match:

                        key_value = key_match.group(1)

                        return key_value

    return None

@app.route('/relzhub/')

def get_key_value():

    link = request.args.get('link')



    

    if not link:

        return jsonify({'error': 'No link provided'})

    

        

    loop = asyncio.new_event_loop()

    start_time = time.time()

    asyncio.set_event_loop(loop)

    key_value = loop.run_until_complete(fetch_key_value(link))

    if key_value:

        end_time = time.time()

        data = {

            "key": key_value,

            "discord": "https://discord.gg/HvvsbpVz7d",

            "credits": "Made by xpython01 and faisal8754",

            "time_taken": round(end_time - start_time, 2)

        }

        return jsonify(data), 200

    else:

        return jsonify({'error': 'Failed to fetch key'})

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=1782)