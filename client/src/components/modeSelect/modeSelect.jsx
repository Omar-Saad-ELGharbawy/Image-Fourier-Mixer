import { Col, Row } from "react-bootstrap";
import Image from "../image/index";
import { defualtImage } from "../../globals/constants/constants";

import { AppContext } from "../../context/index";
import React, { useContext, useEffect } from "react";
import style from "./style.module.css";
import axios from "../../globals/api/axios";

const ModeSelect = ({ type }) => {
  const {
    status,
    setStatus,
    mag1,
    mag2,
    phase1,
    phase2,
    isSelectedPhase1,
    selectPhase1,
    isSelectedPhase2,
    selectPhase2,
    isSelectedMag1,
    selectMag1,
    isSelectedMag2,
    selectMag2,
    setMixedImage,
    setImg1,
    setImg2,
    setMag1,
    setMag2,
    setPhase1,
    setPhase2,
  } = useContext(AppContext);

  const on_click = (isMag) => {
    if (type === 1) {
      if (isMag) {
        selectMag1(!isSelectedMag1);
        selectPhase1(false);
        if (isSelectedMag2) {
          selectMag2(false);
          selectPhase2(true);
        }
      } else {
        selectPhase1(!isSelectedPhase1);
        selectMag1(false);
        if (isSelectedPhase2) {
          selectPhase2(false);
          selectMag2(true);
        }
      }
    } else {
      if (isMag) {
        selectMag2(!isSelectedMag2);
        selectPhase2(false);
        if (isSelectedMag1) {
          selectMag1(false);
          selectPhase1(true);
        }
      } else {
        selectPhase2(!isSelectedPhase2);
        selectMag2(false);
        if (isSelectedPhase1) {
          selectPhase1(false);
          selectMag1(true);
        }
      }
    }
    setStatus(true);

    // send_request();
  };

  const send_request = () => {
    setMixedImage(defualtImage);
    const data = {
      phase_1_selected: isSelectedPhase1,
      phase_2_selected: isSelectedPhase2,
      mag_1_selected: isSelectedMag1,
      mag_2_selected: isSelectedMag2,
    };
    console.log(
      isSelectedMag1,
      isSelectedMag2,
      isSelectedPhase1,
      isSelectedPhase2
    );

    axios.post("/update", data).then((res) => {
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
    <Col>
      <Row
        className={
          type === 1
            ? isSelectedMag1
              ? style.selected
              : style.unselected
            : isSelectedMag2
            ? style.selected
            : style.unselected
        }
      >
        <p className={style.title}>Magnitude</p>
        <button className={style.button} onClick={() => on_click(true)}>
          <Image img={type === 1 ? mag1 : mag2} />
        </button>
      </Row>
      <Row
        className={
          type === 1
            ? isSelectedPhase1
              ? style.selected
              : style.unselected
            : isSelectedPhase2
            ? style.selected
            : style.unselected
        }
      >
        <p className={style.title}>Phase</p>
        <button className={style.button} onClick={() => on_click(false)}>
          <Image img={type === 1 ? phase1 : phase2} />
        </button>
      </Row>
    </Col>
  );
};

export default ModeSelect;
