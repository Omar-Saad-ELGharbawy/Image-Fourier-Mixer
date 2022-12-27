import React, { useRef, useState } from "react";
import style from "./style.module.css";
import Select from "../select/index";
import axios from "../../globals/api/axios";

const UploadImage = ({ type }) => {
  // fetch files from the context

  const inputFileRef = useRef(null);
  const [file, setFile] = useState();
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
      setFile(URL.createObjectURL(inputFile));
      setIsUploaded(true);
      console.log(inputFile);
      upload_image(inputFile);
    }
  };

  const close_image = async (e) => {
    setIsUploaded(false);
    inputFileRef.current.value = null;
    setFile(null);
  };

  const upload_image = async (file) => {
    const formData = new FormData();
    formData.append("file", file);
    console.log(file);
    console.log(formData);
    axios.post("/upload", formData).then((res) => {
      console.log(res.data);
    });
  };

  return (
    <div className={style.container} style={{}}>
      <button
        className={style.close}
        onClick={close_image}
        style={{ visibility: !isUploaded ? "visible" : "hidden" }}
      >
        x
      </button>
      {isUploaded ? (
        <div>
          <Select
            img={<img src={file} alt="" className={style.image} />}
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
