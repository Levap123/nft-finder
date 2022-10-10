from src import create_app


def test_nft_page():
    app = create_app('flask_test.cfg')
    with app.test_client() as test_client:
        response = test_client.get('/api/v1/nft?q=9MyQpAazdSsiNTKYU35kE8RgtCp2ax8XhuLfzr9346pH')
        assert response.status_code == 200
        assert b"ABC #3429" in response.data
