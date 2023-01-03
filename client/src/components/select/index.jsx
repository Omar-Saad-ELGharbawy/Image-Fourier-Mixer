import { AppContext } from "../../context/index";
import React, { useContext } from "react";
import { defualtImage } from "../../globals/constants/constants";
import "react-image-crop/dist/ReactCrop.css";
import ReactCrop from "react-image-crop";
import axios from "../../globals/api/axios";

const Select = ({ img, type }) => {
  // fetch files from the context
  const {
    dimensions1,
    setDimensions1,
    dimensions2,
    setDimensions2,
    setImg1,
    setImg2,

    setMag1,
    setMag2,
    setPhase1,
    setPhase2,
    setMixedImage,
    isSelectIn1,
    isSelectIn2,
  } = useContext(AppContext);

  // Methods
  const on_change = (perc) => {
    axios
      .post("/crop", {
        dimensions: perc,
        type: type,
        isSelectIn: type === 1 ? isSelectIn1 : isSelectIn2,
      })
      .then((res) => {
        console.log(res.data);
        setImg1(res.data.img1 !== "" ? res.data.img1 : defualtImage);
        setMag1(res.data.mag1 !== "" ? res.data.mag1 : defualtImage);
        setPhase1(res.data.phase1 !== "" ? res.data.phase1 : defualtImage);
        setImg2(res.data.img2 !== "" ? res.data.img2 : defualtImage);
        setMag2(res.data.mag2 !== "" ? res.data.mag2 : defualtImage);
        setPhase2(res.data.phase2 !== "" ? res.data.phase2 : defualtImage);
        setMixedImage(
          res.data.mixed_img !== "" ? res.data.mixed_img : defualtImage
        );
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
