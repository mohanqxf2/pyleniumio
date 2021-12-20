
BASE_URL = 'https://reqres.in'

def test_get_demo(py):
    py.visit('https://reqres.in')
    response = py.request.get(f'{BASE_URL}/api/users/2')
    assert response.ok
    assert response.json()['data']['first_name'] == 'Janet'

def test_post_demo(py):
    r =  py.request.post(f'{BASE_URL}/api/users', data = {"name":"mohan","job":"qxf2"})
    assert r.status_code == 201
    assert r.json()['id'] is not None