const getKakaoUserInfo = async () => {
  let data = ""
  await window.Kakao.API.request({
    url: "/v2/user/me",
    success: function (response) {
      data = response
    },
    fail: function (error) {
      console.log(error)
    },
  })
  console.log("카카오 계정 정보", data)
  return data
}

export default getKakaoUserInfo
