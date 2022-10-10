from src import create_app


def test_home_page():
    app = create_app('flask_test.cfg')
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Enter nft address and get information about it!" in response.data
        assert b"Search!" in response.data



