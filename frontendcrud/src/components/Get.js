import React, { useEffect, useState } from "react";
import { Table, Button, Modal } from "antd";
import "antd/dist/antd.css";
import axios from "axios";
import Info from "./Info";
import Create from "./Create";
import Delete from "./Delete";
import Edit from "./Edit";
import "../styles/main.css";

const Get = () => {
  const [data, setData] = useState([]);
  const [post, setPost] = useState(false);
  const [put, setPut] = useState(false);
  const [del, setDel] = useState(false);
  const [info, setInfo] = useState(false);
  const [users, setUsers] = useState({});
  const baseUrl = "http://localhost:8000/api/v1/users";

  const changePost = () => {
    setPost(!post);
  };

  const changePut = () => {
    setPut(!put);
  };

  const changeDel = () => {
    setDel(!del);
  };

  const changeinfo = () => {
    setInfo(!info);
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUsers({ ...users, [name]: value });
  };

  const selectPost = (users, choose) => {
    setUsers(users);
    if (choose === "Edit") {
      changePut();
    } else if (choose === "Delete") {
      changeDel();
    } else changeinfo();
  };

  const getMethod = async () => {
    try {
      const response = await axios.get(baseUrl);
      if(response.data)
      setData(response.data);
      else alert("false")
    } catch (err) {
      alert("Sorry we can't handle this operation");
    }
  };

  const postMethod = async () => {
    delete users.id;
    try {
      const response = await axios.post(baseUrl, users);
      setData(response.data);
      setUsers({})
      console.log(users);
      changePost();
    } catch (err) {
      alert("Sorry we can't handle this operation");
    }
  };
  const putMethod = async () => {
    try {
      const response = await axios.put(baseUrl + "/" + users.id, users);
      setData(response.data);
      changePut()
      setUsers({})
    } catch (error) {
      alert("Sorry we can't handle this operation");
    }
  };
  const delMethod = async () => {
    try {
        const response = await axios.delete(baseUrl + "/" + users.id)
        setData(response.data)
        changeDel()
        setUsers({})
    } catch (error) {
        alert("Sorry we can't handle this operation");   
    }
  };
  useEffect(() => {
    getMethod();
  }, []);
  const columns = [
    {
      title: "Name",
      dataIndex: "name",
      key: "name",
      defaultSortOrder: "descend",
    },
    {
      title: "Email",
      dataIndex: "email",
      key: "email",
    },
    {
      title: "Phone",
      dataIndex: "phone",
      key: "phone",
    },
    {
      title: "Action",
      key: "action",
      width: "15%",
      render: (row) => (
        <>
          <Button onClick={(e) => {selectPost(row, "Info");}}>Info</Button>
          <Button className="mg" type="primary" onClick={(e) => {selectPost(row, "Edit");}}>Edit</Button>
          <Button type="primary" danger onClick={() => selectPost(row, "Delete")}>Delete</Button>
        </>
      ),
    },
  ];
  return (
    <div className="App">
      <div className="button__create">
        <Button type="primary" onClick={changePost}>Create post</Button>
      </div>
      <Table bordered columns={columns} dataSource={data} />
      <Create users={users} post={post} changePost={changePost} postMethod={postMethod} handleChange={handleChange} setUsers={setUsers}/>
      <Edit setUsers={setUsers} users={users} put={put} changePut={changePut} putMethod={putMethod} handleChange={handleChange}/>
      <Delete del={del} changeDel={changeDel} delMethod={delMethod} users={users}/>
      <Modal visible={info} onCancel={changeinfo} centered title="Users info" width="90%" destroyOnClose={true} footer="">
      <Info users={users} /></Modal>
    </div>
  );
};

export default Get;
