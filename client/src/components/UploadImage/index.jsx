import React, { useRef, useState, useContext } from "react";
import style from "./style.module.css";
import Select from "../select/index";
import axios from "../../globals/api/axios";
import { AppContext } from "../../context/index";
import { defualtImage } from "../../globals/constants/constants";

const UploadImage = ({ type }) => {
  // fetch files from the context
  const {
    setImg1,
    setImg2,
    img1,
    img2,
    setMag1,
    setMag2,
    setPhase1,
    setPhase2,
  } = useContext(AppContext);

  const inputFileRef = useRef(null);
  const [isUploaded, setIsUploaded] = useState(false);

  //////////////////////////////////////////////////////
  //Method

  // force input clicking
  const handle_button_click = () => {
    inputFileRef.current.click();
  };

  // handle on upload file
  const handle_file_upload = async (e) => {
    let inputFile = e.target.files[0];
    if (inputFile) {
      if (type === 1) {
        setImg1(URL.createObjectURL(inputFile));
      } else {
        setImg2(URL.createObjectURL(inputFile));
      }
      setIsUploaded(true);
      console.log(inputFile);
      upload_image(inputFile);
    }
  };

  const close_image = async (e) => {
    setIsUploaded(false);
    inputFileRef.current.value = null;
    if (type === 1) {
      setImg1(defualtImage);
      setMag1(defualtImage);
      setPhase1(defualtImage);
    } else {
      setImg2(defualtImage);
      setMag2(defualtImage);
      setPhase2(defualtImage);
    }
  };

  const upload_image = async (file) => {
    const formData = new FormData();
    formData.append("file", file);
    formData.append("type", type);
    console.log(file);
    console.log(formData);
    axios.post("/upload", formData).then((res) => {
      console.log(res.data);
      if (type === 1) {
        setImg1(res.data.img_url);
        setMag1(res.data.mag_url);
        setPhase1(res.data.phase_url);
      } else {
        setImg2(res.data.img_url);
        setMag2(res.data.mag_url);
        setPhase2(res.data.phase_url);
      }
    });
  };

  return (
    <div className={style.container} style={{}}>
      <button
        className={style.close}
        onClick={close_image}
        style={{ visibility: isUploaded ? "visible" : "hidden" }}
      >
        <span className={style.icon}></span>
      </button>
      {isUploaded ? (
        <div>
          <Select
            img={
              <img
                src={type === 1 ? img1 : img2}
                alt=""
                className={style.image}
              />
            }
            type={type}
          />
        </div>
      ) : (
        <button className={style.empty} onClick={handle_button_click}>
          <p>Upload an image</p>
        </button>
      )}

      <input
        type="file"
        accept="image/*"
        id="file"
        ref={inputFileRef}
        style={{ display: "none" }}
        onChange={handle_file_upload}
      />
    </div>
  );
};

export default UploadImage;
