import React, { useRef, useState } from "react";
import style from "./style.module.css";
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
    setFile(null);
  };

  return (
    <div>
      {isUploaded ? (
        <div>
          <button className={style.close} onClick={close_image}>
            x
          </button>
          <img src={file} alt="" className={style.container} />
        </div>
      ) : (
        <button className={style.container} onClick={handle_button_click}>
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
