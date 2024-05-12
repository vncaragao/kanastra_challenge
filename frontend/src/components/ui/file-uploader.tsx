import { ChangeEvent } from "react";

type FileUploaderProps = {
  file?: File;
  setFile: (file: File) => void;
  uploadFile: () => void;
}

const FileUploader = ({ file, setFile, uploadFile }: FileUploaderProps) => {

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    const selectedFile = event.target.files && event.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
    }
  };

  return (
    <div className = "flex flex-col gap-6">
      <div>
        <label htmlFor="file" className="sr-only">
          Choose a file
        </label>
        <input
          id="file"
          type="file"
          accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel,text/csv"
          onChange={handleFileChange}
          />
      </div>
      {file && (
        <section>
          <p className="pb-6">File details:</p>
          <ul>
            <li>Name: {file.name}</li>
            <li>Type: {file.type}</li>
            <li>Size: {file.size} bytes</li>
          </ul>
        </section>
      )}

      {file &&
        <button
          className="rounded-lg bg-green-800 text-white px-4 py-2 border-none font-semibold"
          onClick={uploadFile}
          >Upload the file</button>}
    </div>
  );
};

export { FileUploader };
