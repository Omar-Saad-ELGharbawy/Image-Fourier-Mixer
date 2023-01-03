import React, { useContext, useEffect, useState } from "react";
import style from "./style.module.css";
import BootstrapSwitchButton from "bootstrap-switch-button-react";
import { AppContext } from "../../context/index";
import axios from "../../globals/api/axios";
import { defualtImage } from "../../globals/constants/constants";
const Switch = ({ type }) => {
  const {
    isSelectIn1,
    selectIn1,
    isSelectIn2,
    selectIn2,
    setImg1,
    setImg2,
    setMag1,
    setMag2,
    setPhase1,
    setPhase2,
    setMixedImage,
    dimensions1,
    dimensions2,
  } = useContext(AppContext);

  const [status, setStatus] = useState(false);

  const send_request = () => {
    axios
      .post("/crop", {
        isSelectIn: type === 1 ? isSelectIn1 : isSelectIn2,
        type: type,
        dimensions: type === 1 ? dimensions1 : dimensions2,
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
    setStatus(false);
  };

  useEffect(() => {
    if (status) {
      console.log("sending request");
      send_request();
    }
  }, [status]);

  return (
    <BootstrapSwitchButton
      checked={type === 1 ? isSelectIn1 : isSelectIn2}
      width={200}
      onlabel="Select In"
      offlabel="Select Out"
      onstyle="primary active"
      offstyle="primary"
      style={style.switch}
      onChange={(checked) => {
        if (type === 1) {
          selectIn1(checked);
        } else {
          selectIn2(checked);
        }
        setStatus(true);

        console.log(checked);
        console.log(type);
        console.log(isSelectIn1);
        console.log(isSelectIn2);
      }}
    />
  );
};

export default Switch;
