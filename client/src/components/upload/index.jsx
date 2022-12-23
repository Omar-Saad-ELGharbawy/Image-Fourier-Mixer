import { AppContext } from "../../context/index";
import React, { useContext } from "react";
import style from "./style.module.css";

const Upload = () => {
  // fetch files from the context
  const { status, setStatus } = useContext(AppContext);

  // Methods

  return <div className={style.container}></div>;
};

export default Upload;
