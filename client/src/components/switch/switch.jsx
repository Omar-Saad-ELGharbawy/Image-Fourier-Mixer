import React  from "react";
import style from "./style.module.css"
import BootstrapSwitchButton from 'bootstrap-switch-button-react'

const Switch = () => {
  return (
    <BootstrapSwitchButton  checked={true} onlabel="Low Pass" offlabel="High Pass" onstyle="light" offstyle="light" style={style.switch}/>
  )
}

export default Switch

