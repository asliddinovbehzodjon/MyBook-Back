BASE_URL = 'http://127.0.0.1:8000/api/book/bot/'
import requests
requests.post(url=BASE_URL,data={
    'name':'Behzod',
    't_id':123457
})