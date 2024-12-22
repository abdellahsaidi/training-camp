import React from "react";

const FormSection = ({ fields }) => {
  return (
    <div className="form-section">
      {fields.map((field, index) => (
        <label key={index}>
          {field.label}
          <input type={field.type} placeholder={field.placeholder} />
        </label>
      ))}
    </div>
  );
};

export default FormSection;
