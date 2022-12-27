import { AppContext } from "../context/index";
import React, { useContext } from "react";
import style from "./style.module.css";
import Image  from "../components/image";



const Layout = () => {
  return (
    <div>
      <div className={style.first_wrapper}>
        <div className={style.top_left}><Image /></div>
        <div className={style.top_right}><Image /></div>
      </div>
      <div className={style.second_wrapper}>
        <div className={style.bottom}></div>
      </div>
    </div>
  );
};

export default Layout;
