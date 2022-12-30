import Image from "../image/index";
import style from "./style.module.css";
import { AppContext } from "../../context/index";
import React, { useContext } from "react";

const OutputImage = () => {
  const { mixedImage } = useContext(AppContext);

  return (
    <div className={style.OutputImage}>
      <Image img={mixedImage} />
    </div>
  );
};

export default OutputImage;
