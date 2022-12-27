import { AppContext } from "../context/index";
import React, { useContext } from "react";
import style from "./style.module.css";
import UploadImage from "../components/UploadImage/index";
import Image from "../components/image";
import { Col, Row, Container } from 'react-bootstrap'
import ModeSelect from "../components/modeSelect/modeSelect"

const Layout = () => {
  return (
    <Container fluid>
      <Row>
      
      <Col xs={6} sm={6} md={6} lg={6} >
          <Row>
          <Col xs={8} sm={8} md={8} lg={8}><UploadImage img={<Image/> }type={1}/></Col>
          <Col xs={4} sm={4} md={4} lg={4}>
          <ModeSelect/>
    </Col>
          
          </Row>
        </Col>  
         
      <Col xs={6} sm={6} md={6} lg={6} >
          <Row>
          <Col xs={8} sm={8} md={8} lg={8}><UploadImage img={<Image/> }type={1}/></Col>
          <Col xs={4} sm={4} md={4} lg={4}>
            <Row><Image/><Row>
            </Row><Image/></Row>
          </Col>
          </Row>
        </Col> 

      </Row>


      <Row>
        <Col><Image/></Col>
      </Row>
    </Container>



  );
};

export default Layout;
{/* <div>
 <div className={style.first_wrapper}>
<div className={style.top_left}><Image /></div>
<div className={style.top_right}><Image /></div>
</div>
<div className={style.second_wrapper}>
<div className={style.bottom}></div>
</div>
</div>  */}