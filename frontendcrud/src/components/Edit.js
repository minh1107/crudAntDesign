import React from "react";
import { Modal, Button, Input, Form } from "antd";
import "antd/dist/antd.css";
import "../styles/main.css";

const { Item } = Form;
const Edit = ({users, put, changePut, putMethod, handleChange, setUsers}) => {
  const lb = {
    labelCol: {span: 4}, wrapperCol:{span: 18}
  }
  const onFinish = () => {
    putMethod();
    setUsers({});
  };
  const onFinishFailed = () => {
    alert('Please enter information')
    setUsers({});
  };
  return (
    <div>
      <Modal width="60%" visible={put} title="Edit user" onCancel={changePut} centered footer={[]}>
        <Form name="basic" initialValues={{ remember: true, }}  {...lb}  onFinish={onFinish} onFinishFailed={onFinishFailed} >
          <Item label="Name">
            <Input
              disabled="false" name="name" onChange={handleChange} value={users && users.name}/>
          </Item>
          <Item label="Username">
            <Input
              disabled="false" name="username" onChange={handleChange} value={users && users.username}/>
          </Item>
          <Form.Item label="Email" 
            rules={[
              {
                required: true,
                message: "Please input your email!",
                type: "email",
              }
            ]}>
            <Input
              name="email" onChange={handleChange} value={users && users.email} />
          </Form.Item>
          <Item label="Phone">
            <Input
              name="phone" onChange={handleChange} value={users && users.phone}/>
          </Item>
          <Item label="Website">
            <Input
              name="website" onChange={handleChange} value={users && users.website}/>
          </Item>
          <Item className="bold_text" label="Address" />
          <Form {...lb}>
            <Item label="Street">
              <Input
                name="addressstreet" onChange={handleChange} value={users && users.addressstreet}/>
            </Item>
            <Item label="Suite">
              <Input
                name="addresssuite" onChange={handleChange} value={users && users.addresssuite}/>
            </Item>
            <Item label="City">
              <Input
                name="addresscity" onChange={handleChange} value={users && users.addresscity}/>
            </Item>
            <Item label="Zip code">
              <Input name="addresszipcode" onChange={handleChange} value={users && users.addresszipcode}/>
            </Item>
          </Form>
          <Item label="Company" className="bold_text" />
          <Form {...lb}>
            <Item label="Name company">
              <Input name="companyname" onChange={handleChange} value={users && users.companyname} ></Input>
            </Item>
            <Item label="Catch Phrase">
              <Input name="companycatchphrase" onChange={handleChange} value={users && users.companycatchphrase}></Input>
            </Item>
            <Item label="Business">
              <Input name="companybs" onChange={handleChange} value={users && users.companybs}></Input>
            </Item>
          </Form>
          <Form.Item className="center_form">
          <Button className="postMethod" onClick={changePut}>Cancel</Button>
          <Button type="primary" htmlType="submit">Edit</Button>
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
};

export default Edit;
