import { AppContext } from "../../context/index";
import React, { useContext, useState } from "react";
// import style from "./style.module.css";
import "react-image-crop/dist/ReactCrop.css";
import ReactCrop from "react-image-crop";
import axios from "../../globals/api/axios";

const Select = ({ img, type }) => {
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

  const on_change = (c) => {
    axios.post("/update", { dimensions: c }).then((res) => {
      console.log(res.data);
    });
  };

  return (
    <ReactCrop
      crop={crop}
      onComplete={(crop, perc) => {
        console.log(crop, perc);
        on_change(perc);
      }}
      onChange={(c) => {
        setCrop(c);
      }}
    >
      <img src={img} style={{ width: "50%" }} alt="img" />
    </ReactCrop>
  );
};

export default Select;
