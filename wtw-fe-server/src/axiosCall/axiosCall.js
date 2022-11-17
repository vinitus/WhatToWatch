import axios from "axios"

const API_URL = "http://localhost:8000"

export default async function axiosCall(path, method, data = "") {
  let result = await axios({
    url: `${API_URL}/${path}`,
    mehtod: method,
    data: data,
  }).then((res) => res.data)

  return result
}
