import { AppContext } from "../../context/index";
import React, { useContext } from "react";
import style from "./style.module.css";

const Image = () => {
  // fetch files from the context
  // const { status, setStatus } = useContext(AppContext);
  // Methods
  return (
    <div className={style.container}>
        <div className={style.block1}><h1 className={style.original_photo}>Orignal Photo</h1></div>
        <div className={style.block2}><h1>Phase</h1></div>
        <div className={style.block3}><h1>Magnitude</h1></div> 
    </div>
  ); 
};

export default Image;
