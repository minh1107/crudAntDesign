import React from "react";
import { Modal, Button, Input, Form } from "antd";
import "antd/dist/antd.css";

const { Item } = Form;
const Create = ({
  post, setUsers, changePost, postMethod, handleChange,}) => {
  const onFinish = () => {
    postMethod();
    setUsers({});
  };
  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
    setUsers({});
  };
  const lb = {
    labelCol: {span: 4}, wrapperCol:{span: 18}
  }
  return (
    <div>
      <Modal width="60%" visible={post} title="Insert post" destroyOnClose={true} onCancel={changePost} centered footer="">
        <Form name="basic" initialValues={{ remember: true, }} onFinish={onFinish} onFinishFailed={onFinishFailed} autoComplete="off" {...lb}>
          <Form.Item name="name" label="Name" rules={[
              { required: true,
                message: "Please input your name!",
              },
            ]}>
            <Input onChange={handleChange} placeholder="Enter name" name="name"/>
          </Form.Item>
          <Form.Item label="Username" name="username" 
            rules={[
              {
                required: true,
                message: "Please input your username!",
              },
            ]}>
            <Input name="username" onChange={handleChange} placeholder="Enter username" />
          </Form.Item>
          <Item
            label="Email" name="email" 
            rules={[
              {
                required: true,
                message: "Please input your email!",
                type: "email",
              },
            ]}
          >
            <Input name="email" onChange={handleChange} placeholder="Enter email" />
          </Item>
          <Item label="Phone">
            <Input name="phone" onChange={handleChange} placeholder="Enter phone"/>
          </Item>
          <Item label="Website">
            <Input name="website" onChange={handleChange} placeholder="Enter website"/>
          </Item>
          <Item label="Address"></Item>
          <Form {...lb}>
            <Item label="Street">
              <Input placeholder="Enter street address" name="addressstreet" onChange={handleChange}/>
            </Item>
            <Item label="Suite">
              <Input name="addresssuite" onChange={handleChange} placeholder="Enter suite address"/>
            </Item>
            <Item label="City">
              <Input name="addresscity" onChange={handleChange} placeholder="Enter city address"/>
            </Item>
            <Item label="Zip code">
              <Input name="addresszipcode" onChange={handleChange} placeholder="Enter zip code address"/>
            </Item>
          </Form>
          <Item label="Company"></Item>
          <Form {...lb}>
            <Item label="Name">
              <Input name="companyname" onChange={handleChange} placeholder="Enter name company"></Input>
            </Item>
            <Item label="Catch Phrase">
              <Input name="companycatchphrase" onChange={handleChange} placeholder="Enter catch phrase company"></Input>
            </Item>
            <Item label="Business">
              <Input name="companybs" onChange={handleChange} placeholder="Enter business company"></Input>
            </Item>
          </Form>
          <Form.Item className="center_form">
            <Button className="postMethod" onClick={changePost}>Cancel</Button>
            <Button type="primary" htmlType="submit">Create user</Button>
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
};

export default Create;
