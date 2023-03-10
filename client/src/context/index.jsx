import { defualtImage } from "../globals/constants/constants";
import React, { createContext, useState } from "react";
export const AppContext = createContext();

export const FileContextProvider = ({ children }) => {
  // Test
  const [value, setValue] = useState(0);

  // App Data
  const [status, setStatus] = useState(false);
  const [img1, setImg1] = useState(defualtImage);
  const [img2, setImg2] = useState(defualtImage);
  const [dimensions1, setDimensions1] = useState({
    unit: "%",
    width: 0,
    height: 0,
    x: 0,
    y: 0,
  });
  const [dimensions2, setDimensions2] = useState({
    unit: "%",
    width: 0,
    height: 0,
    x: 0,
    y: 0,
  });
  const [mag1, setMag1] = useState(defualtImage);
  const [mag2, setMag2] = useState(defualtImage);
  const [phase1, setPhase1] = useState(defualtImage);
  const [phase2, setPhase2] = useState(defualtImage);
  const [mixedImage, setMixedImage] = useState(defualtImage);
  const [isSelectedPhase1, selectPhase1] = useState(false);
  const [isSelectedPhase2, selectPhase2] = useState(false);
  const [isSelectedMag1, selectMag1] = useState(false);
  const [isSelectedMag2, selectMag2] = useState(false);
  const [isSelectIn1, selectIn1] = useState(true);
  const [isSelectIn2, selectIn2] = useState(true);

  return (
    <AppContext.Provider
      value={{
        value,
        setValue,
        status,
        setStatus,
        img1,
        setImg1,
        img2,
        setImg2,
        dimensions1,
        setDimensions1,
        dimensions2,
        setDimensions2,
        mag1,
        setMag1,
        mag2,
        setMag2,
        phase1,
        setPhase1,
        phase2,
        setPhase2,
        isSelectedPhase1,
        selectPhase1,
        isSelectedPhase2,
        selectPhase2,
        isSelectedMag1,
        selectMag1,
        isSelectedMag2,
        selectMag2,
        mixedImage,
        setMixedImage,
        isSelectIn1,
        selectIn1,
        isSelectIn2,
        selectIn2,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};
