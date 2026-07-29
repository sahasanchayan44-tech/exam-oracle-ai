import { NestFactory } from '@nestjs/core';
import { ValidationPipe, Logger } from '@nestjs/common';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import { AppModule } from './app.module';
import { HttpExceptionFilter } from './common/filters/http-exception.filter';
import { LoggingInterceptor } from './common/interceptors/logging.interceptor';

async function bootstrap() {
  const logger = new Logger('Bootstrap');
  const app = await NestFactory.create(AppModule);

  // Global Prefix
  const apiPrefix = process.env.API_PREFIX || 'api/v1';
  app.setGlobalPrefix(apiPrefix);

  // CORS Configuration
  app.enableCors({
    origin: process.env.CORS_ORIGIN || 'http://localhost:3000',
    credentials: true,
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE,OPTIONS',
  });

  // Global Pipes, Filters & Interceptors
  app.useGlobalPipes(
    new ValidationPipe({
      whitelist: true,
      transform: true,
      forbidNonWhitelisted: true,
    }),
  );
  app.useGlobalFilters(new HttpExceptionFilter());
  app.useGlobalInterceptors(new LoggingInterceptor());

  // OpenAPI / Swagger Documentation Setup
  const config = new DocumentBuilder()
    .setTitle('Exam Oracle AI - API Gateway')
    .setDescription(
      'Enterprise API for Exam Paper Analysis, Bayesian Topic Probability Estimation, and Practice Question Synthesis.',
    )
    .setVersion('1.0.0')
    .addBearerAuth()
    .addTag('Authentication')
    .addTag('Papers')
    .addTag('Probability Analytics')
    .addTag('Practice Generation')
    .build();

  const document = SwaggerModule.createDocument(app, config);
  SwaggerModule.setup(`${apiPrefix}/docs`, app, document);

  const port = process.env.API_GATEWAY_PORT || 4000;
  await app.listen(port);
  logger.log(`API Gateway listening on http://localhost:${port}/${apiPrefix}`);
  logger.log(`Swagger OpenAPI Documentation: http://localhost:${port}/${apiPrefix}/docs`);
}

bootstrap();
