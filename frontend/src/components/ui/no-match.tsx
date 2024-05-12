import { ReactElement, useEffect, useState } from "react";
import { FileUploader } from "./file-uploader";
import { ListFiles, InsertNewFile } from "@/controllers/FileController";
import { IFileList } from "./types";
import { Table, TableBody, TableCell, TableFooter, TableHead, TableRow } from "./table";

function NoMatch(): ReactElement {

  const [fileList, setFileList] = useState<IFileList[]>([])
  const [file, setFile] = useState<File| undefined>(undefined);

  async function getFiles() {
    const result = await ListFiles();
    setFileList(result);
  }

  async function uploadFile(){
    if (file) {
      await InsertNewFile(file);
      setFile(undefined);
      getFiles();
    }
  }

  useEffect(() => {
    const interval = setInterval(() => {
      getFiles()
    }, 600000);
    getFiles()
    return () => clearInterval(interval);
  }, [])


  return (
    <div className="h-screen w-screen bg-zinc-800 text-white gap-6 flex flex-1 flex-col items-center justify-center">
      <FileUploader file={file} setFile={setFile} uploadFile={uploadFile}/>
      {fileList.length > 0 ? (
        <Table>
          <TableBody>
            <TableRow>
              <TableHead>ARQUIVO</TableHead>
              <TableHead>ULTIMA ATUALIZAÇÃO</TableHead>
              <TableHead>Nº DE ITENS</TableHead>
              <TableHead>STATUS</TableHead>
            </TableRow>
            {fileList.map((file) => (
              <TableRow>
                <TableCell>{file.filename}</TableCell>
                <TableCell>{file.last_update}</TableCell>
                <TableCell>{file.items}</TableCell>
                <TableCell>{file.status}</TableCell>
              </TableRow>
            ))}
            <TableFooter></TableFooter>
          </TableBody>
        </Table>
      ) : (
        <h1>Não há items para exibir.</h1>
      )}
    </div>
  );
}

export { NoMatch }
