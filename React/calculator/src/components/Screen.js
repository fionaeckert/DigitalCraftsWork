import { Textfit } from "react-textfit";
import "./Screen.css";

const Screen = ({ value }) => {
  return (
    <Textfit className="screen" mode="single" max={70}>
      <Screen value={calc.num ? calc.num : calc.res} />
    </Textfit>
  );
};

export default Screen;