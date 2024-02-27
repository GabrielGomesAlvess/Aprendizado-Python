create table categoria (
  codigo int not null  auto_increment,
  nome varchar(45) not null,
  primary key(codigo)
  );
  
create table status_cliente (
  codigo int not null  auto_increment,
  nome varchar(45) not null,
  primary key(codigo)
  ); 
  
create table produto (
  codigo int not null auto_increment,
  nome varchar(100) not null,
  preco decimal(11,2) not null,
  estoque int,
  categoria_codigo int not null,
  primary key (codigo),
  foreign key (categoria_codigo) references categoria(codigo)
  );
  
create table cliente (
  codigo int not null auto_increment,
  nome varchar(100) not null,
  endereco varchar(200) not null,
  telefone varchar(20) not null,
  limite decimal(11,2) not null,
  status_cliente_codigo int not null,
  primary key(codigo),
  foreign key(status_cliente_codigo) references status_cliente(codigo)
  );
    
  