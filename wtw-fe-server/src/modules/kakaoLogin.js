import axios from "axios"

const kakaoHeader = {
  Authorization: "cb807e086b62ee4f422b02a65e4017ed",
  "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
}

const getKakaoToken = async (code) => {
  console.log("loginWithKakao")
  try {
    const data = {
      grant_type: "authorization_code",
      client_id: "9e23cba329b4a051b6a8d2fa14e8ddf2",
      redirect_uri: "http://localhost:8080/auth",
      code: code,
    }
    const queryString = Object.keys(data)
      .map((k) => encodeURIComponent(k) + "=" + encodeURIComponent(data[k]))
      .join("&")
    const result = await axios.post(
      "https://kauth.kakao.com/oauth/token",
      queryString,
      { headers: kakaoHeader }
    )
    console.log(1)
    console.log("카카오 토큰", queryString)
    return result
  } catch (e) {
    return e
  }
}

export default getKakaoToken
