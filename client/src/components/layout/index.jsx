import style from "./style.module.css";
import UploadImage from "../UploadImage/index";
import Image from "../image";
import { Col, Row, Container } from "react-bootstrap";
import ModeSelect from "../modeSelect/modeSelect";
import OutputImage from "../outputImage/outputImage";
import { AppContext } from "../../context/index";
import React, { useContext } from "react";

const Layout = () => {
  const { img1, img2 } = useContext(AppContext);

  return (
    <Container fluid className={style.container}>
      <Row>
        <Col xs={6} sm={6} md={6} lg={6}>
          <Row>
            <Col xs={5} sm={5} md={5} lg={5}>
              <ModeSelect type={1} />
            </Col>
            <Col xs={7} sm={7} md={7} lg={7}>
              <UploadImage img={img1} type={1} />
            </Col>
          </Row>
        </Col>

        <Col xs={6} sm={6} md={6} lg={6}>
          <Row>
            <Col xs={7} sm={7} md={7} lg={7}>
              <UploadImage img={img2} type={2} />
            </Col>
            <Col xs={5} sm={5} md={5} lg={5}>
              <ModeSelect type={2} />
            </Col>
          </Row>
        </Col>
      </Row>
      <Row className={style.output}>
        <Col xs={4} sm={4} md={4} lg={4} className={style.outputCol}>
          <OutputImage />
        </Col>
      </Row>
    </Container>
  );
};

export default Layout;
