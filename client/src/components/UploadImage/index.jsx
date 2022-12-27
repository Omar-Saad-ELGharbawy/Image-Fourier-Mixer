import React, { useRef, useState } from "react";
import "./style.css";

const UploadImage = () => {
  const inputFileRef = useRef(null);
  const [file, setFile] = useState();
  const [isUploaded, setIsUploaded] = useState(false);
  // force input clicking
  const handleButtonClick = () => {
    inputFileRef.current.click();
  };

  // handle on upload file
  const handleFileUpload = async (e) => {
    let inputFile = e.target.files[0];
    if (inputFile) {
      setFile(URL.createObjectURL(inputFile));
      setIsUploaded(true);
      console.log(inputFile);
    }
  };

  return (
    <div className="upload-audio">
      <button onClick={handleButtonClick} style={{ width: "300px", height: "300px", backgroundColor: "#fd5c63" , border:"none", borderRadius:"15px"}}>
        {isUploaded ? (
          <img src={file} alt="" style={{ width: "300px", height: "300px", borderRadius:"15px" }} />
        ) : (
          <div
            // style={{ width: "300px", height: "300px", backgroundColor: "#E9967A" , border:"none", borderRadius:"10px", display:"flex", alignContent:"center", alignItems:"center"}}
          >
            <div style={{ color:"white", position:"relative", left:"0%", fontSize:"20px"}}>
            Upload an image
            </div>
          </div>
        )}
      </button>

      <input
        type="file"
        accept="image/*"
        id="file"
        ref={inputFileRef}
        style={{ display: "none" }}
        onChange={handleFileUpload}
      />
    </div>
  );
};

export default UploadImage;
