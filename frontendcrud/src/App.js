import React, { useEffect, useState } from "react";
import { Table, Button, Modal, Input, Form } from "antd";
import "antd/dist/antd.css";
import "./App.css";
import axios from "axios";
import Info from "./components/Info";
import Create from "./components/Create";
import Delete from "./components/Delete";
import Edit from "./components/Edit";

const { Item } = Form;

function App() {
  const [data, setData] = useState([]);
  const [insertMethod, setInsertMethod] = useState(false);
  const [editMethod, setEditMethod] = useState(false);
  const [deleteMethod, setDeleteMethod] = useState(false);
  const [infoMethod, setInfoMethod] = useState(false);
  const [users, setUsers] = useState({});

  const baseUrl = "http://localhost:8000/api/v1/users";
  const deleteUrl = "http://localhost:8000/api/v1/delete"
  const postUrl = "http://localhost:8000/api/v1/create/user";
  const putUrl = "http://localhost:8000/api/v1/users";

  const changeInsertMethod = () => {
    setInsertMethod(!insertMethod);
  };

  const changeEditMethod = () => {
    setEditMethod(!editMethod);
  };

  const changeDeleteMethod = () => {
    setDeleteMethod(!deleteMethod);
  };

  const changeInfoMethod = () => {
    setInfoMethod(!infoMethod);
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    console.log(name, value);
    setUsers({ ...users, [name]: value });
    console.log(users)
  };

  const selectPost = (users, choose) => {
    setUsers(users);
    if (choose === "Edit") {
      changeEditMethod();
    } else if (choose === "Delete") {
      changeDeleteMethod();
    } else changeInfoMethod();
  };

  const getMethod = async () => {
    await axios
      .get(baseUrl)
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };


  const postMethod = async () => {
    delete users.id;
    try {
      const response = await axios.post(postUrl, users);
      let item = [];
      setData(item.concat(response.data));
      changeInsertMethod();
    } catch (err) {
      console.log(err);
    }
  };
  // put
  const putMethod = async () => {
    await axios
      .put(putUrl + "/" + users.id, users)
      .then((response) => {
        setData(response.data);
        changeEditMethod();
      })
      .catch((error) => {
        console.log(error);
      });
  };
  //delete method
  const methodDelete = async () => {
    console.log(users);
    await axios.delete(deleteUrl + "/" + users.id)
      .then((response) => {
        getMethod();
        changeDeleteMethod();
      })
      .catch((error) => {
        console.log(error);
      });
  };

  useEffect(() => {
    getMethod();
  }, []);
  const columns = [
    {
      title: "Name",
      dataIndex: "name",
      key: "name",
      defaultSortOrder: 'descend',
      sorter: (a, b) => a.name.length - b.name.length,
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
        // button edit delete
        <>
          <Button
            onClick={(e) => {
              selectPost(row, "Info");
            }}
          >
            Info
          </Button>
          <Button
            className="mg"
            type="primary"
            onClick={(e) => {
              selectPost(row, "Edit");
            }}
          >
            Edit
          </Button>
          <Button
            type="primary"
            danger
            onClick={() => selectPost(row, "Delete")}
          >
            Delete
          </Button>
        </>
      ),
    },
  ];

  return (
    <div className="App">
      <br />
      <br />
      <Button
        type="primary"
        className="botonInsertar"
        onClick={changeInsertMethod}
      >
        Create post
      </Button>
      <br />
      <br />
      {/* table onclick changeInfoMethod */}
      <Table bordered columns={columns} dataSource={data} />
      {/* chen */}
      <Create
        // handleChangeCompanyName = {handleChangeCompanyName}
        users={users}
        insertMethod={insertMethod}
        changeInsertMethod={changeInsertMethod}
        postMethod={postMethod}
        handleChange={handleChange}
        setUsers={setUsers}
      />
      {/* Edit */}
      <Edit
        users={users}
        editMethod={editMethod}
        changeEditMethod={changeEditMethod}
        putMethod={putMethod}
        handleChange={handleChange}
        // handleChangeCompanyName={handleChangeCompanyName}
      />
      {/* delete */}
      <Delete
        deleteMethod={deleteMethod}
        changeDeleteMethod={changeDeleteMethod}
        methodDelete={methodDelete}
        users={users}
      />
      {/* Info */}
      <Modal
        visible={infoMethod}
        onCancel={changeInfoMethod}
        centered
        title="Users info"
        width="90%"
        destroyOnClose={true}
        footer=""
      >
        <Info users={users} />
      </Modal>
    </div>
  );
}

export default App;
