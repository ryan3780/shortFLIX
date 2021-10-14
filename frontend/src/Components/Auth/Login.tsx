import React, { useState } from "react";
import axios from "axios";
import "./scss/Login.scss";
import Logo from "../Assets/Image/shortFLIX.png";
import { useHistory } from "react-router";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faUserAlt, faKey } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

library.add(faUserAlt, faKey);

const Login = () => {
  const [id, setId] = useState("");
  const [password, setPassword] = useState("");
  const history = useHistory();
  const onChangeHandler = (e: { target: { name: any; value: any } }) => {
    const {
      target: { name, value },
    } = e;
    if (name === "id") {
      setId(value);
      console.log(id);
    } else if (name === "password") {
      setPassword(value);
      console.log(password);
    }
  };
  const URL =
    "http://kdt-vm-0202003.koreacentral.cloudapp.azure.com:5000/login";
  const onLoginHandler = (event: { preventDefault: () => void }) => {
    event.preventDefault();
    axios
      .post(URL, {
        email: id,
        password: password,
      })
      .then((response: any) => {
        if (response.status === 200) {
          console.log(response.data);
          sessionStorage.setItem("username", response.data);
          history.push("/");
        }
      });
  };
  return (
    <div className="Login__Container">
      <div className="Login__Contents">
        <img className="Login__Logo" src={Logo} alt="" />
        <form className="Login__Form" action="">
          <div>
            <label htmlFor="id">
              <FontAwesomeIcon icon={faUserAlt} />
            </label>
            <input
              id="id"
              type="email"
              required
              placeholder="이메일을 입력하세요."
              name="id"
              autoComplete="off"
              value={id}
              onChange={onChangeHandler}
            />
          </div>
          <div>
            <label htmlFor="password">
              <FontAwesomeIcon icon={faKey} />
            </label>
            <input
              id="password"
              type="password"
              name="password"
              value={password}
              required
              placeholder="비밀번호를 입력하세요."
              onChange={onChangeHandler}
            />
          </div>

          <button type="submit" onClick={onLoginHandler}>
            로그인
          </button>
          <div className="Login__Register">
            <span>아이디가 없으신가요?</span>
            <a href="/register">회원가입</a>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;