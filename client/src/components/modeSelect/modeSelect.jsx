import { Col, Row } from "react-bootstrap";
import Image from "../image/index";
import { AppContext } from "../../context/index";
import React, { useContext } from "react";
import style from "./style.module.css";
const ModeSelect = ({ type }) => {
  const {
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
  } = useContext(AppContext);

  const on_click = (isMag) => {
    if (isMag) {
      if (type === 1) {
        selectMag1(!isSelectedMag1);
      } else {
        selectMag2(!isSelectedMag2);
      }
    } else {
      if (type === 1) {
        selectPhase1(!isSelectedPhase1);
      } else {
        selectPhase2(!isSelectedPhase2);
      }
    }
    console.log(
      isSelectedMag1,
      isSelectedMag2,
      isSelectedPhase1,
      isSelectedPhase2
    );
    console.log(type, isMag);
  };
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
        <button className={style.button} onClick={() => on_click(false)}>
          <Image img={type === 1 ? phase1 : phase2} />
        </button>
      </Row>
    </Col>
  );
};

export default ModeSelect;
