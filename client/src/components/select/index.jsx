import { AppContext } from "../../context/index";
import React, { useContext } from "react";
// import style from "./style.module.css";
import "react-image-crop/dist/ReactCrop.css";
import ReactCrop from "react-image-crop";
import axios from "../../globals/api/axios";

const Select = ({ img, type }) => {
  // fetch files from the context
  const { dimensions1, setDimensions1, dimensions2, setDimensions2 } =
    useContext(AppContext);

  // Methods
  const on_change = (perc) => {
    axios.post("/crop", { dimensions: perc, type: type }).then((res) => {
      console.log(res.data);
    });
  };

  return (
    <ReactCrop
      crop={type === 1 ? dimensions1 : dimensions2}
      onComplete={(crop, perc) => {
        console.log(crop, perc);
        on_change(perc);
      }}
      onChange={(px, prec) => {
        if (type === 1) {
          setDimensions1(prec);
        } else {
          setDimensions2(prec);
        }
      }}
    >
      {img}
    </ReactCrop>
  );
};

export default Select;
