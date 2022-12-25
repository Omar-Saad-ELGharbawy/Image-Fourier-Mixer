import { AppContext } from "../../context/index";
import React, { useContext, useState } from "react";
import style from "./style.module.css";
import "react-image-crop/dist/ReactCrop.css";
import ReactCrop from "react-image-crop";
import img from "../../globals/assets/0.jpg";

const Select = () => {
  // fetch files from the context
  const { status, setStatus } = useContext(AppContext);
  const [crop, setCrop] = useState({
    unit: "%",
    width: 100,
    height: 100,
    x: 0,
    y: 0,
  });
  // Methods

  return (
    <ReactCrop
      crop={crop}
      onDragStart={(e) => {
        console.log(e);
      }}
      onComplete={(crop, perc) => {
        console.log(crop, perc);
      }}
      onChange={(c) => {
        setCrop(c);
        // console.log(c);
      }}
    >
      <img src={img} style={{ width: "800px" }} alt="img" />
    </ReactCrop>
  );
};

export default Select;
