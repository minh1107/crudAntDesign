import requests

if __name__ == '__main__':
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NDYzMjg5Nzh9.rSjqkQzlIsNpftgTeeNnSnSmfPGRj_1lCZ5C6ByNfDw"
    for i in range(0, 1):
        response = requests.get("http://localhost:8000/api/v1/products/ping", headers={
            "Authorization": f"Bearer {token}"
        })
        print(response.text)
