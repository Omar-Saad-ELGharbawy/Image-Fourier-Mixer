import { AppContext } from "../../context/index";
import React, { useContext } from "react";
import style from "./style.module.css";
import img from "../../globals/assets/img.png";
const Image = () => {
  // fetch files from the context
  // const { status, setStatus } = useContext(AppContext);
  // Methods
  return <img className={style.imageContainer} src={img} alt="" />;
};

export default Image;
