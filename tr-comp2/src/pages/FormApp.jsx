import React from "react";
import FormContainer from "../components/FormContainer";
import HeaderFr2 from "../components/HeaderFr2";
import Sidebar2 from "../components/Sidebar2";

const FormApp = () => {
  return (
    <div>
      <Sidebar2 />
      <div>
        <HeaderFr2 />
        <FormContainer />
      </div>
    </div>
  );
};

export default FormApp;
