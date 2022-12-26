import React from "react";
import Select from "../components/select";
// import Test from "../components/test/index";
import img from "../globals/assets/0.jpg";

const Layout = () => {
  return (
    <div>
      <Select
        img={<img src={img} style={{ width: "800px" }} alt="img" />}
        type={1}
      />
    </div>
  );
};

export default Layout;
