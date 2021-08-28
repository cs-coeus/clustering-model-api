# Clustering Model

This is an API service for `ModelClustering` of `coeus`

## API Documentation
### `GET /heathcheck`
Request: `None`

Response: `'OK'` with HTTP Status `200`

### `POST /predict`
Request:
`"data"` is an array with three elements.
- The first element is an array of string represent all documents in corpus.
- The second element is length of an array in the first element.
- The third element is proximity matrix.
```json
{
  "data": [
    ["sentence 1", "sentence 2", "sentence 3"], 
    3,
    [[0, 0.5, 0.5], [0.5, 0, 0.5], [0.5, 0.5, 0]]
  ]
}
```
Response:
`"result"` is an array with two elements.
- The first element is the most appropriate number of cluster K.
- The second element is the clusters result from choosing K cluster(s). Each one is cluster id for that particular sentence.
```json
{
  "result": [
    3,
    [0, 1, 2]
  ]
}
```

## Run
1. Copy file `.env.example` into `.env` and fill in all necessary values
2. Make sure you have Docker installed on your system and running
3. Build Docker image with a name of your choice if you haven't
```shell
docker build --tag clustering-api .
```
5. Spin up a server
```shell
docker run -d -p 5000:5000 --name clustering-api clustering-api
```
6. Try accessing [http://127.0.0.1:5000](http://127.0.0.1:5000) with a valid route