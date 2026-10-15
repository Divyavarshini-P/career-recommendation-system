import { useDropzone } from "react-dropzone";
import "../styles/FileUpload.css";

function FileUpload({ resumeFile, setResumeFile }) {

  const onDrop = (acceptedFiles) => {
    if (acceptedFiles.length > 0) {
      setResumeFile(acceptedFiles[0]);
    }
  };

  const { getRootProps, getInputProps, isDragActive } =
    useDropzone({
      onDrop,
      accept: {
        "application/pdf": [".pdf"],
        "application/msword": [".doc"],
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": [".docx"],
      },
      multiple: false,
    });

  return (
    <div
      {...getRootProps()}
      className={`dropzone ${isDragActive ? "active" : ""}`}
    >
      <input {...getInputProps()} />

      {resumeFile ? (
        <>
          <h2>✅ Resume Selected</h2>
          <p>{resumeFile.name}</p>
        </>
      ) : (
        <>
          <h2>📄 Drag & Drop Resume</h2>
          <p>or click to browse</p>
          <small>Supports PDF and DOCX</small>
        </>
      )}
    </div>
  );
}

export default FileUpload;