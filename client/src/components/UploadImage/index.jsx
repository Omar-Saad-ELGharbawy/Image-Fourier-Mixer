import React, { useRef, useState } from "react";
import style from "./style.module.css";
import Select from "../select/index";
const UploadImage = () => {
  const inputFileRef = useRef(null);
  const [file, setFile] = useState();
  const [isUploaded, setIsUploaded] = useState(false);
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
    }
  };
  const close_image = async (e) => {
    setIsUploaded(false);
    inputFileRef.current.value = null;
    setFile(null);
  };

  return (
    <div className={style.container}>
      <button
        className={style.close}
        onClick={close_image}
        style={{ visibility: isUploaded ? "visible" : "hidden" }}
      >
        x
      </button>
      {isUploaded ? (
        <div>
          <Select
            img={<img src={file} alt="" className={style.image} />}
            type={1}
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
