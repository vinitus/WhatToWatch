import axios from "axios"
import API_KEY from "@/modules/secret.js"

const kakaoHeader = {
  "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
}

const getKakaoToken = async (code) => {
  console.log("loginWithKakao")
  try {
    const data = {
      grant_type: "authorization_code",
      client_id: API_KEY.client_id,
      redirect_uri: "http://localhost:8080/auth",
      code: code,
    }
    const queryString = Object.keys(data)
      .map((k) => encodeURIComponent(k) + "=" + encodeURIComponent(data[k]))
      .join("&")
    const result = await axios.get(
      `https://kauth.kakao.com/oauth/token?${queryString}`,
      {
        headers: kakaoHeader,
      }
    )
    return result
  } catch (e) {
    console.log(e)
    return e
  }
}

export default getKakaoToken
