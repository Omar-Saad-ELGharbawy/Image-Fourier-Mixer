import React  from "react";
import style from "./style.module.css"
import BootstrapSwitchButton from 'bootstrap-switch-button-react'

const Switch = () => {
  return (
    <BootstrapSwitchButton  
    checked={true} 
    width={200}
    onlabel="Low Pass" 
    offlabel="High Pass" 
    onstyle="light active" 
    offstyle="light active" 
    style={style.switch}/>
  )
}

export default Switch

