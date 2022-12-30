import { Col, Row } from "react-bootstrap";
import Image from "../image/index";
import { AppContext } from "../../context/index";
import React, { useContext } from "react";
const ModeSelect = ({ type }) => {
  const { mag1, mag2, phase1, phase2 } = useContext(AppContext);

  return (
    <Col>
      <Row>
        <Image img={type === 1 ? mag1 : mag2} />
      </Row>
      <Row>
        <Image img={type === 1 ? phase1 : phase2} />
      </Row>
    </Col>
  );
};

export default ModeSelect;
