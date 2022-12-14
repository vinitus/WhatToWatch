import axios from "axios"

const API_URL = "http://localhost:8000"

export default async function axiosCall(path, method, data, headers) {
  let result = await axios({
    url: `${API_URL}/${path}`,
    method: method,
    data: data,
    headers: headers,
  }).then((res) => res.data)

  return result
}
