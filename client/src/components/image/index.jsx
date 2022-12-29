import style from "./style.module.css";
const Image = ({ img }) => {
  return <img className={style.imageContainer} src={img} alt="" />;
};

export default Image;
